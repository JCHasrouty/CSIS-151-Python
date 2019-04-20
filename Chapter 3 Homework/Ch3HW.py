# Chapter 3 Homework Assignment
# Programmer: Jean Claude Hasrouty
# Instructor: Zare Agazaryan
# CSIS 151
# Date Created: 3/10/18

user_height = int(input("Please enter your height: \n"))
if user_height < 0:
    print("That's an invalid height.")
else:
    user_weight = int(input("Please enter your weight: \n"))
    if user_weight < 0:
        print("That's an invalid weight.")
    else:
        bmi = (user_weight * 703)/ user_height ** 2

        if (bmi >= 18.5) and (bmi <= 25):
            print("BMI =", format(bmi, "2.2f"))
            print("You are optimal.")

        elif (bmi < 18.5):
            print("BMI =", format(bmi, "2.2f"))
            print("You are underweight.")
        
        else:
            print("BMI =", format(bmi, "2.2f"))
            print("You are overweight.")


