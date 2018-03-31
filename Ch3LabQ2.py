# Chapter 3 Lab Question 2
# Programmer: Jean Claude Hasrouty
# Instructor: Zare Agazaryan
# CSIS 151
# Date Created: 3/6/18

user_input = input("Please enter a number 1..10: \n")

if int(user_input) == 1:
    print("The roman numeral for " + user_input + " is I.")
elif int(user_input) == 2:
    print("The roman numeral for " + user_input + " is II.")
elif int(user_input) == 3:
    print("The roman numeral for " + user_input + " is III.")
elif int(user_input) == 4:
    print("The roman numeral for " + user_input + " is IV.")
elif int(user_input) == 5:
    print("The roman numeral for " + user_input + " is V.")
elif int(user_input) == 6:
    print("The roman numeral for " + user_input + " is VI.")
elif int(user_input) == 7:
    print("The roman numeral for " + user_input + " is VII.")
elif int(user_input) == 8:
    print("The roman numeral for " + user_input + " is VIII.")
elif int(user_input) == 9:
    print("The roman numeral for " + user_input + " is IX.")
elif int(user_input) == 10:
    print("The roman numeral for " + user_input + " is X.")
else:
    print("That's not a valid number.")
