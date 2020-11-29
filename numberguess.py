import random

introstring = int(input("Guess a number between 1 and 9:-"))
print(introstring)
randomNo = random.randint(0,9)
chances = 0

while chances < 5:
    if(introstring == randomNo):
        print("You are correct")
        break
    elif(introstring > randomNo):
         print("Your number is greater than the given number.")
         break
    else: 
        print("Your number is less than the given number.")
        break
    chances = chances +1
if not chances < 5:
    print("Sorry you lose")
    
