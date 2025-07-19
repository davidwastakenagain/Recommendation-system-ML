
print("Hello")
import pandas as pd
import random
# Predefined lists
#names = ['Alice', 'Bob', 'Charlie']
#ages = [25, 30, 22]
#cities = ['New York', 'San Francisco', 'Los Angeles']

# Create a Data Frame
#data = {'Name': ['names'], 'Age': ['ages'], 'City': ['cities']}
#df = pd.DataFrame(data)

# Display the Data Frame
#print(df)

user = ["Qian Yi","Kai","Zikun","Abeinaian","Eric"]
movie1 = []
movie2 = []
movie3 = []
movie4 = []
movie5 = []
data = {}
def create_dataframe():

    for x in range(5):
        a = random.randint(1,5)
        movie1.append(a)
        b = random.randint(1, 5)
        movie2.append(b)
        c = random.randint(1, 5)
        movie3.append(c)
        d = random.randint(1, 5)
        movie4.append(d)
        e = random.randint(1, 5)
        movie5.append(e)

    #Display the Data Frame
    data = {"User":user,
            "Star Wars":movie1,
            "Shrek":movie2,
            "Iron man":movie3,
            "Inside out": movie4,
            "Scary movie":movie5

            }

    df = pd.DataFrame(data)
    print(df)
    
create_dataframe()