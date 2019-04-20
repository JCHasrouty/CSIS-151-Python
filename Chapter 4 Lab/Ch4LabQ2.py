# Chapter 4 Lab Question 2
# Programmer: Jean Claude Hasrouty
# Instructor: Zare Agazaryan
# CSIS 151
# Date Created: 3/6/18

current_pay = 0.01
total_pay = 0

num_days = int(input("Please enter the number of worked days:\n"))
while (num_days < 1) or (num_days > 60):
    print("Invalid number of days.")
    num_days = int(input("Enter the number of days again:\n"))
                                      
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
