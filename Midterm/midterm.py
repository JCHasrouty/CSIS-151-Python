def main():
    filename = ask_filename()

    while not file_exists(filename) and filename.upper() != "QUIT":
        print("File:", filename, "does not exist.")
        filename = ask_filename_again()

    if filename.upper() != "QUIT":
        readContents(filename)

def ask_filename_again():
    filename = input("Please enter the file name again or type QUIT to exit:\n")
    return filename

def ask_filename():
    filename = input("Please enter the file name or type QUIT to exit:\n")
    return filename

def file_exists(filename):
    try:
        file = open(filename)
        file.close()
    except FileNotFoundError:
        file_ok = False
    else:
        file_ok = True
        
    return file_ok

def readContents(filename):
    file = open(filename, 'r')
    count = 0
    totalSum = 0
    # count amount of lines extracted from file
    line = file.readline()
    if line == '':
        print("File", filename, "is empty.")
        return
    else:
        while line != '':
            file_info = float(line)
            totalSum += file_info
            count += 1
            
            line = file.readline()

    average = totalSum / count
    print("Count:", count)
    print("Total:", format(totalSum, ",.3f"))
    print("Average:", format(average, ",.3f"))
    file.close()
    
main()

