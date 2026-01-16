# THE PERFECT GUESS

import random
def Guess_number(user_no,Rand_no):
    
    if (Rand_no < user_no):
        print("Lower number please!")
        return False
    elif(Rand_no > user_no):
        print("Higher number please!")
        return False
    else:
        return True
    

#choose a random integer between 1 to 10  
Rand_no = random.randint(1,10)  

print("Welcome to the number guessing game!")

attempts =0  # attempts initially is zero to guess the correct number 

while True:
     
     user_no = int(input("Enter the number between 1 to 10:"))
     attempts +=1  
     if Guess_number(user_no,Rand_no):
         print(f"Congratulation! You guess the number in {attempts} attempts")
         break
         



        





