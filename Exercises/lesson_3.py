#lowercase loop
import time
from collections import Counter
import math
'''
friends = ["Alice", "Bob", "Charlie"]

for i in range(len(friends)):
    lower = friends[i].lower()
    print(lower)

for friend in friends:
    if friend[0] == "A":
        print(f"Hello {friend}")

    else:
        print(f"goodbye {friend}")

for i in range(10):
    if i == 9:
        print("this is the end")

# Sum all numbers in a list
numbers = [1, 2, 3, 4, 5]
somme = 0
for num in numbers:
    somme = somme + num

print(somme)
somme = 0
while True:
    num = int(input("enter a number: "))
    somme += num
    if num == 0:
        break
print(somme)
'''

# Print only the common elements from the following two lists:
#healthy_food = ["apple", "salmon", "avocado", "seafood", "olive oil", "spinach", "yogurt"]
#vegan_food = ["cookies", "apple", "avocado", "candy", "olive oil", "fake chicken", "spinach"]
#for health in healthy_food:
    #for vegan in vegan_food:
        #if health == vegan:
            #print(health)

'''count = 10
for i in range(10):
    time.sleep(1)
    print(count)
    count -= 1
    
    if count == 1:
        print("Blast off!")
        continue'''

'''num = 99
while True:
    print(f"{num} bottles of pop on the wall  {num} bottles of pop If one of those bottles should happen to fall,")
    num -= 1
    if num == 0:
        print("No more bottles of pop on the wall, no more bottles of pop. Go to the store and buy some more, 99 bottles of pop on the wall...")
        break

contacts = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}

name = input("Enter your contact name: ")
if name in contacts:
    print(contacts[name])

else:
    print("Contact not found")'''

'''friends = ['David','Alexander','Edmond','Evan', 'Luka',
           'Triston','Kourosh','Catherine','Kateryna', 'Sai']
favorite_movies = [
    ['Interstellar','Minions'],
    ['Cars','Batman'],
    ['Tenet','The Pianist'],
    ['Titanic'],
    ['Batman','Titanic'],
    ['The Edge of Tomorrow','Black Hawk Down'],
    ['John Wick','Minions'],
    ['Inception','Seven Samurai'],
    ['Flow','Die Hard'],
    ['Wolf of Wallstreet', 'Ready Player One']
]'''

'''friends = ["Alice", "Bob", "Charlie"]
movie_rating = {
            "Minions": [1,2,3],
            "Intercept":[3,2,1,]
            "The last edge": [2,1,3]
                
                
                }'''

'''student_grades = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "Diana": 88,
    "Ethan": 95
}
average = 0

for student,grade in student_grades.items():
    print(f'{student} got {grade}')
    average = average + grade

print(f"the average is {average/len(student_grades)}")'''
'''
sentence = input('enter a sentence: ')
sentence.lower()
words = Counter(sentence.split())
print(words)'''

'''celsius_values = [-40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for x in range(len(celsius_values)):
    fah_values = (celsius_values[x] * 4.5) + 32'''

def mystery7(lst):
    return [x for x in lst if isinstance(x, int) and x % 2 == 0]

print(mystery7([1, 2, 3, 4, 5, 6, "eight", 10]))

