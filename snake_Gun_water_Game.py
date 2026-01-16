# SNAKE , WATER OR GUN GAME

import random

def gamewin(comp, user):
    if(comp == "snake"):
        if(user == "water"):
            return False
        elif(user == "gun"):
            return True
        else:
            return None
    elif(comp == "water"):
        if(user == "snake"):
            return True
        elif(user == "gun"):
            return False
        else:
            return None
    elif(comp == "gun"):
        if(user == "snake"):
            return False
        elif(user == "water"):
            return True
        else: 
            return None

print("Snake Water or Gun Game")
print("Game Elements:\nSnake: Represents a snake.\nWater: Represents water.\nGun: Represents a gun.")
print("Rules: \nSnake beats by Gun : Gun shot the Snake then Snake is die. \nGun beats by  Water:  Gun sank inside the Water.\nWater beats by Snake: Snake drinked the Water")


n = int(input("Enter wants to be the no of rounds : "))
s = input("Enter 's' to Start the game:")
u = 0   # User Score
c = 0  #computer Score
t = 0  # Tie Score
if(s=='s' or s=='S'):
    for i in range(1,n+1):
           user = input("Enter your choice :")
           list = ['snake', 'gun' , 'water']
           comp = random.choice(list)
           print(f"Computer choice is :{comp}")
           if(gamewin(comp,user) == True):
                print(f"You Win {i} round ")
                u+=1
           elif(gamewin(comp,user) == False):
                print(f"You Lose {i} round")
                c+=1 
           elif(gamewin(comp,user) == None):
                print(f"{i} round is Tie ")
                t+=1

if(u>c):
    print("Congratultion , You win the game")
    print(f"Score out of {n} rounds is : \n{u} : ROUNDS win \n{c} : ROUNDS lose \n{t} : ROUNDS tie ")
elif(c>u):
    print("You've lost the game ! Better luck for next time")
    print(f"Score out of {n} rounds is : \n{u} : ROUNDS win \n{c} : ROUNDS lose \n{t} : ROUNDS tie ")
else:
    print("Game Tie! , This game is Tie")
    print(f"Score out of {n} rounds is : \n{u} : ROUNDS win \n{c} : ROUNDS lose \n{t} : ROUNDS tie ")