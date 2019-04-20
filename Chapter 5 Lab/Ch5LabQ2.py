# Chapter 5 Lab Q2
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

user_num = int(input("Enter a number: \n"))
    
for p in range(2, user_num + 1):
    if isPrime(p):
        print(p, end=" ") 
