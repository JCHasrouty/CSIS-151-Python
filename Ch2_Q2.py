# Chapter 2 Question 2
# Programming Challenge #8 Tip, Tax, and Total
# Programmer: Jean Claude Hasrouty
# Date Created: 3/3/2018
tax_rate = 0.07
tip_percent = 0.18
meal_cost = float(input("Please enter the charge for the food: \n"))
subtotal = meal_cost
tax_amount = subtotal * tax_rate
tip_amount = meal_cost * tip_percent
total = subtotal + tax_amount + tip_amount
print("Subtotal:\t$", format(subtotal, "8,.2f"), sep = '')
print("Tax(", format(tax_rate * 100, ".2f"), "%):\t$", format(tax_amount, "8,.2f"), sep = '') # separator takes out spaces 
print("Tip(", format(tip_percent * 100, ".2f"), "%):\t$", format(tip_amount, "8,.2f"), sep = '') #
print("============", "  ", "=========")
print("Total:\t\t$", format(total, "8,.2f"), sep = '')


