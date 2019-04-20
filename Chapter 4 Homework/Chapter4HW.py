# Chapter 4 Homework Assignment
# Programmer: Jean Claude Hasrouty
# Instructor: Zare Agazaryan
# CSIS 151
# Date Created: 3/20/18

sum_total = 0

user_num = 0

while (user_num >= 0):

    user_num = float(input("Enter a positive number to add or negative number to finish:\n"))
    if (user_num >= 0):
        sum_total += user_num

print("Total:", format(sum_total, "2.1f"))
    
