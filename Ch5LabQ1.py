# Chapter 5 Lab Q1
# Programmer: Jean Claude Hasrouty
# Instructor: Zare Agazaryan
# CSIS 151
# Date Created: 3/20/18

def isPrime(num):
    if num > 1:
        for n in range(2,num):
            if num % n == 0:
                return False
                break
        return True
        
user_num = 0 
while(user_num >= 0):
    user_num = int(input("Enter a number for primality test (or a negative number to exit): \n"))
    if(user_num < 0):
        break
    elif(isPrime(user_num) == True):    
        print("Number", user_num, "is a prime number.")
    else:
        print("Number", user_num, "is not a prime number.")


    
