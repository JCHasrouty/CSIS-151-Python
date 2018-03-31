# Chapter 2 Homework Assignment
# Programmer: Jean Claude Hasrouty
# Instructor: Zare Agazaryan
# CSIS 151
# Date Created: 3/10/18

user_input = float(input("Please enter a temperature in Celsius:\n"))

c_to_f = 9/5*(user_input) + 32

print(format(user_input, ".1f"), "Celsius =", format(c_to_f, ".1f"), "Fahrenheit")
