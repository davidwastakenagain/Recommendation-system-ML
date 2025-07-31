import discord
from discord.ext import commands
import pandas as pd
from surprise import Reader, Dataset, SVD, accuracy
from surprise.model_selection import train_test_split
import random
import nest_asyncio 
import asyncio
nest_asyncio.apply()
import numpy as np
from dotenv import load_dotenv
import os
import openai
import time
load_dotenv()
MY_TOKEN = os.getenv("DISCORD_TOKEN")

openai.api_key = os.getenv("ai_API")


df_movies =  pd.read_csv("movies.csv")
df_ratings =  pd.read_csv("ratings.csv")

user_threads = {}
assistant_id = None


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
  print(f'{bot.user} is now online!')
  print(f"Registered commands: {[command.name for command in bot.commands]}")

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message) 

def create_assistant():
    assistant = openai.beta.assistants.create(
        name="Discord AI",
        instructions="You're a helpful assistant for explaining AI and programming concepts.",
        model="gpt-4o"
    )
    return assistant.id

def create_thread():
    thread = openai.beta.threads.create()
    return thread.id

def send_message_to_assistant(assistant_id, thread_id, user_message):
    openai.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_message
    )
    run = openai.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )
    return run.id

async def wait_for_response(thread_id, run_id):
    while True:
        run_status = openai.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
        if run_status.status == "completed":
            break
        elif run_status.status == "failed":
            raise Exception("Run failed.")
        await asyncio.sleep(1) 

    messages = openai.beta.threads.messages.list(thread_id=thread_id)
    for msg in messages.data:  
        if msg.role == "assistant":
            return msg.content[0].text.value
    return "No assistant response found."

# Create the assistant once at bot startup
assistant_id = create_assistant()


@bot.command(name="askai")
async def ask_openai(ctx, *, prompt):
    try:
        await ctx.send("Thinking...")

        user_id = ctx.author.id
        thread_id = user_threads.get(user_id)
        if not thread_id:
            thread_id = create_thread()
            user_threads[user_id] = thread_id

        run_id = send_message_to_assistant(assistant_id, thread_id, prompt)
        reply = await wait_for_response(thread_id, run_id)

        await ctx.send(reply)

    except Exception as e:
        await ctx.send(f"Error: {e}")

@bot.command(name = "search_movie")
async def search(ctx,movie_name):
    matches = df_movies[df_movies["title"].str.contains(movie_name, case=False)]
    if matches.empty:
        await ctx.send("No movies found.")
    else:
        result = "\n".join([f"{row['movieId']}: {row['title']}" for _, row in matches.iterrows()])
        await ctx.send(f"Found:\n{result}\nUse `!rate <movieId> <rating>` to rate.")
    
    
@bot.command(name = "rate")
async def rate(ctx, movie_id: int, rating: float):
    if rating > 5 or rating < 0:
        await ctx.send("Ratings must be between 0 and 5")
    user_id = ctx.author.id  
    new_row = pd.DataFrame([[user_id, movie_id, rating]], columns=["userId", "movieId", "rating"])
    global df_ratings

    df_ratings = pd.concat([df_ratings, new_row], ignore_index=True)
    df_ratings.to_csv("ratings.csv", index=False)
    await ctx.send(f"Rated movie {movie_id} with {rating} stars.")
    


@bot.command(name="recommend")
async def recommend(ctx, n: int = 5):
    user_id = ctx.author.id
    user_ratings = df_ratings[df_ratings['userId'] == user_id]
    
    if len(user_ratings) < 5:
        await ctx.send("You need to rate at least 5 movies for personalized recommendations.")
        return

    reader = Reader(rating_scale=(0, 5))
    data = Dataset.load_from_df(df_ratings[['userId', 'movieId', 'rating']], reader)

    trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

    model = SVD()
    model.fit(trainset)

    all_movie_ids = set(df_movies['movieId'])
    rated_movie_ids = set(user_ratings['movieId'])
    unrated_movie_ids = list(all_movie_ids - rated_movie_ids)

    predictions = []
    for mid in unrated_movie_ids:
        pred = model.predict(user_id, mid)
        predictions.append((mid, pred.est))

    top_predictions = sorted(predictions, key=lambda x: x[1], reverse=True)[:n]

    response = "🎬 **Recommended movies for you:**\n"
    for movie_id, est_rating in top_predictions:
        title = df_movies[df_movies['movieId'] == movie_id]['title'].values[0]
        response += f"- {title} _(predicted rating: {est_rating:.2f})_\n"

    await ctx.send(response)



#max n of movies gnerated was 37

bot.run(MY_TOKEN)