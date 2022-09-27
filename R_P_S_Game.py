#This is my Rock Paper Scissors game
from asyncore import ExitNow
import random

namelist = ("rock", "paper", "scissors")

computerGuess = random.choice(namelist)

#Uncomment Below to see computers guess
#print(computerGuess)

userguess = input(str("Guess rock, paper, or scissors = "))
    
if str(computerGuess) == str(userguess):
    print ("Woops you cant choose the same thing!")
#else:
#   print ("Not a match")

if str(computerGuess) == str("rock") and str(userguess) == str("paper"):
    print("Congrats Paper Beats Rock")
elif str(computerGuess) == str("scissors") and str(userguess) == str("rock"):
    print("Congrats Rock Beats Scissors")
elif str(computerGuess) == str("paper") and str(userguess) == str("scissors"):
    print("Congrats Scissors Beats Paper")
else:
    print("Sorry You Lose :(")
    
print("The Computers guess was")
print(computerGuess)




