def main():
    # open file for reading
    inFile = open('GirlNames.txt', 'r')
    inFile2 = open('BoyNames.txt', 'r')
    girl_list = readContents(inFile)
    boy_list = readContents(inFile2)

    name_search = input("Enter a name to search or type QUIT to exit:\n").lower()
    new_name = name_search.capitalize()
    
    while name_search.upper() != "QUIT":
        if searchList(girl_list, new_name) and not searchList(boy_list, new_name):
            print("The name '", new_name, "' was found in popular girl names list (line ", girl_list.index(new_name) + 1, ").", sep='')
        
        elif searchList(boy_list, new_name) and not searchList(girl_list, new_name):
            print("The name '", new_name, "' was found in popular boy names list (line ", boy_list.index(new_name) + 1, ").", sep='')

        elif searchList(girl_list, new_name) and searchList(boy_list, new_name):
            print("The name '", new_name, "' was found in both lists: boy names (line ", boy_list.index(new_name) + 1, ") and girl names (line ", girl_list.index(new_name) + 1, ").", sep='')

        else:
            print("The name '", new_name, "' was not found in either list.", sep='')

        name_search = input("Enter a name to search or type QUIT to exit:\n").lower()
        new_name = name_search.capitalize()
        
def readContents(filename):
    new_list = []
    new_list = filename.readlines()

    index = 0
    while index < len(new_list):
        new_list[index] = new_list[index].rstrip('\n')
        index += 1

    filename.close()
    return new_list

def searchList(name_list, search_value):
    if search_value in name_list:
        return True
    else:
        return False
    
main()
