# Chapter 6 Lab Q2
# Programmer: Jean Claude Hasrouty
# Instructor: Zare Agazaryan
# CSIS 151
# Date Created: 3/27/18

file_name = ""
operation_done = False
file_name = input("Please enter the file name or type QUIT to exit:\n")
while(not operation_done and file_name != "QUIT" and file_name != "quit"):
        try:
            inFile = open(file_name, 'r')
            count = 1
            file_info = inFile.readline()
            while(file_info != '' and count <= 4):
                print(count, ": ",file_info, end="", sep='')
                count += 1
                file_info = inFile.readline()
            print("")               
    
            inFile.close()
            operation_done = True
        except FileNotFoundError:
            print("File:", file_name, "does not exist.")
            file_name = input("Please enter the file name again or type QUIT to exit:\n")
