def main():
    girl_list = [] * 200
    boy_list = [] * 200
    # open file for reading
    inFile = open('GirlNames.txt', 'r')
    inFile2 = open('BoyNames.txt', 'r')
    # read file contents into list
    girl_list = inFile.readlines()
    boy_list = inFile2.readlines()
    inFile.close()
    inFile2.close()

    print(girl_list)

main()
