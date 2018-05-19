## chapter 9 homework 
## make a dictionary with the key being the employeee name and the value a list
## value is a dictionary also but will contain EID, dept, salary etc

# Global constants for menu choices
import pickle

ADD_EMP = 1
FIND_BN = 2
FIND_BY_EID = 3
DEL_EMP = 4
DISP_STATS = 5
DISP_EMP = 6
QUIT = 7

def main():
    # initialize empty dictionary
    user_input = 0
    employees = load('employee.dat')
    while user_input != QUIT:
        # display menu
        user_input = get_menu_choice()

        if user_input == ADD_EMP:
            addEmployee(employees)
            
        elif user_input == FIND_BN:
            findEmpByName(employees)
            
        elif user_input == FIND_BY_EID:
            findEmpByEID(employees)
            
        elif user_input == DEL_EMP:
            deleteEmployee(employees)
            
        elif user_input == DISP_STATS:
            dispStats(employees)
            
        elif user_input == DISP_EMP:
            dispEmployees(employees)
            
        # for debugging purposes
        # print(employees)
    save(employees, 'employee.dat')
    
def get_menu_choice():
    print("Employee Database")
    print("-----------------")
    print("1. Add an Employee")
    print("2. Find an Employee (By Name)")
    print("3. Find an Employee (By EID)")
    print("4. Delete an Employee")
    print("5. Display Statistics")
    print("6. Display All Employees")
    print("7. Exit")
    print()

    user_input = int(input("Please enter your choice: "))

    while user_input < ADD_EMP or user_input > QUIT:
        user_input = int(input("Please enter a valid choice: "))

    return user_input

def load(filename):
    try:
        file = open(filename, 'rb')
        #unpickle the file and return that dictionary
        unpickled_dictionary = pickle.load(file)
        file.close()
        print("File was read returning loaded dictionary")
        return unpickled_dictionary
    except FileNotFoundError:
        empty_dictionary = {}
        print("Returning empty dictionary")
        return empty_dictionary

def save(dictionary, filename):
    output_file = open(filename, 'wb')
    pickle.dump(dictionary, output_file)
    output_file.close()
    print("Data has been written to file.")
    
def addEmployee(dictionary):
    new_emp = input("Please enter the employees name or type quit to cancel: ")
    # While adding an employee you should allow the user to either cancel the operation
    # or re-enter the name again.
    while new_emp.upper() != "QUIT":
        if new_emp not in dictionary:
            emp_info = input("Please enter the employees ID, Department, Title, and Salary: ")
            dictionary[new_emp] = emp_info
        else:
            print("Employee employee already exists.")
        new_emp = input("Please enter another employee name or type quit to cancel: ")
    print()
        
def findEmpByName(dictionary):
    # lowercase entire word then capitalize first letter and search
    emp_to_find = input("Please enter the name of the employee you'd like to find: ")
    emp_insensitive = emp_to_find.lower().capitalize()
    #print(emp_insensitive)
    print("Employee:", emp_insensitive, dictionary.get(emp_insensitive, "Not found."))
    print()
          
def findEmpByEID(dictionary):
    # function is broken
    emp_eid = input("Please enter the EID of the employee you'd like to find: ")
    for key, value in dictionary.items():
        if value == emp_eid:
            print("Employee:", key,value)
        else:
            print("Employeee was not found.")
def deleteEmployee(dictionary):
    # made this function case insensitive as well
    emp_name = input("Enter an employee name to remove: ")
    emp_insensitive = emp_name.lower().capitalize()
    if emp_insensitive in dictionary:
        del dictionary[emp_insensitive]
    else:
        print("That employee was not found.")
    print()
        
def dispStats(dictionary):
    print("This function is functional but not yet implemented... stay tuned.")
    
def dispEmployees(dictionary):
    for key in dictionary:
        print(key, dictionary[key])
    print()
    
main()
