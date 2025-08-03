#x = 5
#if x > 5:
    #print("x is greater than 5")
#else:
    #print("x is not greater tahn 5")
#print("hello world!")

#functions

#qian = ["Minions","Minions 2","Minion 3"]
#sai =["Ready player one","Paw Patrol","Jujutsu Kaisen"]
#kai = ["Humpty Dumpty","Ne Zha","Ne Zha 2"]
#eric = ["Interstellar","James Bond","Wolf of Wall Street"]
#friends = [qian,sai,kai,eric]
#print(f"My friend {friends[1]} likes {sai[0]}, {sai[1]} and {sai[2]} ")


#friends.append("Baowei")
#friends.pop(3)
#del friends[0]
#friends.insert(2,"Eric")
#print(friends)

#shopping list

#bag = []
#while True:
    #item = input("enter item:")
    #bag.append(item)
    #choice = input("do you want to keep shopping?(yes/no):")
    #if choice == "no":
        #break
    
#print(bag)

friends = ['David','Alexander','Edmond','Evan', 'Luka',
           'Triston','Kourosh','Catherine','Kateryna', 'Sai']

for i in range(len(friends)):
    lower = friends[i].lower()
    print(lower)
    

