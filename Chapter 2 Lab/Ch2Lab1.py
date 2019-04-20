# Chapter 2 Lab 1
# Programming Challenge #4 Total Purchase
# Programmer: Jean Claude Hasrouty
# Date Created: 3/3/2018
tax_rate = 0.07
print("You'll be purchasing 5 items.")
item1 = float(input("Please enter the price of item 1: "))
item2 = float(input("Please enter the price of item 2: "))
item3 = float(input("Please enter the price of item 3: "))
item4 = float(input("Please enter the price of item 4: "))
item5 = float(input("Please enter the price of item 5: "))
subtotal = item1 + item2 + item3 + item4 + item5
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount
print("Subtotal:\t$", format(subtotal, "10,.2f"), sep = '')
print("Tax (", format(tax_rate * 100, ".2f"), "%):\t$", format(tax_amount, "10,.2f"), sep = '') # separator takes out spaces 
print("Total:\t\t$", format(total, "10,.2f"), sep = '')


