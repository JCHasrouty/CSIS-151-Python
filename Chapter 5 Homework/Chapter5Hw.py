# Chapter 5 Lab Q2
# Programmer: Jean Claude Hasrouty
# Instructor: Zare Agazaryan
# CSIS 151
# Date Created: 3/20/18
import random

def compChoice(cp_num):
    if cp_num == 1:
        cp_choice = "rock"
    elif cp_num == 2:
        cp_choice = "paper"
    else:
        cp_choice = "scissors"
    return cp_choice

def isWinner(cp_choice, user_choice):
    if(cp_choice == user_choice):
        print("Its a draw, play again")
    elif (cp_choice == "rock"):
        if(user_choice == "scissors"):
            print("Rock wins")
        else:
            print("Paper wins")
    elif (cp_choice == "scissors"):
        if(user_choice == "paper"):
            print("Scissor wins")
        else:
            print("Rock wins")
    elif (cp_choice == "paper"):
        if(user_choice == "rock"):
            print("Paper wins")
        else:
            print("Scissors wins")
        
comp_num = random.randint(1,3)
user_choice = input("Please choose rock, paper, or scissors: ")
print("You chose", user_choice)
print("The computer chose", compChoice(comp_num))

#determining winner
isWinner(compChoice(comp_num), user_choice)


