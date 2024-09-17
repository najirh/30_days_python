"""
### Mini Project

Project: Number Guessing Game

Project Description:

The program will randomly select a number between 1 and 20. The player will have a limited number 
of chances (let’s say 5) to guess the number. After each guess, the program will tell the player 
whether their guess is too high or too low. If the player guesses correctly within the allowed 
number of attempts, they win. Otherwise, the game ends and the player loses.
"""


# importing dependencies

import random

correct_number = random.randint(1, 20)

print("Welcome to the number guessing game")
print("I am thinking a number between 1 to 20. You have 5 attempt to guess it correctly if you win i will give $1000")


attemp = 5

while attemp > 0:
    
    # collecting numbers
    num = int(input("please guess the number :"))
    
    if num == correct_number:
        print("Congrats you won $1000")
        break
    
    elif num > correct_number:
        print("Your number is too high")
        
    else:
        print("Your number is low")
        
    # reducing the attemp
    attemp -=1
    
    print(f"Your attemp left {attemp}")
    
    if attemp == 0:
        print(f"You are attemp finished! You lost the game. \n The correct number was {correct_number}")
        
    # end
    

