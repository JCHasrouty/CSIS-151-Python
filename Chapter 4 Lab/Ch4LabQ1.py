# Chapter 4 Lab Question 1
# Programmer: Jean Claude Hasrouty
# Instructor: Zare Agazaryan
# CSIS 151
# Date Created: 3/6/18

num_days = int(input("Please enter the number of worked days:\n"))
current_pay = 0.01
total_pay = 0
for x in range(0, num_days):
    if x == 0:  
        current_pay = 0.01
        print("Day: ", x + 1, ","," Payment: $", format(current_pay, "2.2f"), sep='')
        total_pay += current_pay
    else:
        current_pay *= 2
        print("Day: ", x + 1, ","," Payment: $", format(current_pay, "2.2f"), sep='')
        total_pay += current_pay

print("Total: $", format(total_pay, "2.2f"), sep='')
