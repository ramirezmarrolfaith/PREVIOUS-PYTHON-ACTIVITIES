from random import randint

num=randint(1,10)

guess=0

while num != guess:
    guess=eval(input("Guess the number between 1 and 10:"))
    
    if guess>num:
        print("Too high. Try again.")
        
    elif guess<num:
        print("Too low. Try again.")
     
     else:
         print("Congratulations! You got it!")
         
choice=input("Do you want to try again? [y  or type any key to exit]")

while choice=="y" or choice=="Y":
    choice=""
    
from random import randint

num=randint(1,10)

guess=0

while num != guess:
    guess=eval(input("Guess the number between 1 and 10:"))
    
    if guess>num:
        print("Too high. Try again.")
        
    elif guess<num:
        print("Too low. Try again.")
     
     else:
         print("Congratulations! You got it!")
         
choice=input("Do you want to try again? [y  or type any key to exit]")
    