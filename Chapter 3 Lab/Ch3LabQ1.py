# Chapter 3 Lab Question 1
# Programmer: Jean Claude Hasrouty
# Instructor: Zare Agazaryan
# CSIS 151
# Date Created: 3/6/18

user_input = input("Please enter the number of the day (1..7): ")

if int(user_input) == 1:
    print("Monday")
elif int(user_input) == 2:
    print("Tuesday")
elif int(user_input) == 3:
    print("Wednesday")
elif int(user_input) == 4:
    print("Thursday")
elif int(user_input) == 5:
    print("Friday")
elif int(user_input) == 6:
    print("Saturday")
elif int(user_input) == 7:
    print("Sunday")
else:
    print(user_input, "is not in the range 1..7.")
    print("Please re-run the program and enter a valid value.")
