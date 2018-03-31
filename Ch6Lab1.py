# Chapter 6 Lab Q1
# Programmer: Jean Claude Hasrouty
# Instructor: Zare Agazaryan
# CSIS 151
# Date Created: 3/20/18
##        The program should display only the first five lines of the file’s contents.
##        If the file contains less than five lines, it should display the file’s entire contents.

file_name = ""
operation_done = False
while(not operation_done):
    file_name = input("Please enter the file name or type QUIT to exit: ")
    if(file_name != "QUIT" and file_name != "quit" and file_name != "QuiT"):
        try:
            inFile = open(file_name, 'r')
            count = 4
            file_info = inFile.readline()
            while(file_info != '' and count >= 0):
                count -= 1
                print(file_info.rstrip('\n'))
                file_info = inFile.readline()
            inFile.close()
            operation_done = True
        except FileNotFoundError:
            print("File", file_name, "does not exist.")
    else:
        operation_done = True
