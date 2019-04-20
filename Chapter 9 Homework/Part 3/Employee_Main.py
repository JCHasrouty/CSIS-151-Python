import Employee
import pickle

ADD_EMP = 1
FIND_BN = 2
FIND_BY_EID = 3
DEL_EMP = 4
DISP_STATS = 5
DISP_EMP = 6
QUIT = 7

def main():
    employees = load('employee.dat')
    user_input = 0
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
    while new_emp.upper() != "QUIT":
        if new_emp not in dictionary:
            emp_id = input("Please enter the employees ID: ")
            emp_dept = input("Please enter the employees department: ")
            emp_job = input("Please enter the employees job title: " )
            emp_salary = input("Please enter the employees salary: ")
            emp_info = Employee.Employee(emp_id, emp_dept, emp_job, emp_salary)
            dictionary[new_emp] = emp_info
            print(new_emp, "has been successfully added")
        else:
            print("Employee", new_emp,"already exists.")
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
    emp_eid = input("Please enter the EID of the employee you'd like to find: ")
    for (key,value) in dictionary.items():
        if value.get_emp_ID() == emp_eid:
            print("Employee:", key,value)
            print()
            return
    print("Employeee was not found.")
    print()

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
    dept_dict = {}
    max_salary = "Max Salary"
    min_salary = "Min Salary"
    avg = "Average Salary"
    sal_count = "Salary Count"
    total_sal = "Total Salary"

    temp_dict = {} #salaries
    salary_avg = 0
    salary_counter = 0       

    #This initializes all the departments
    for key, value in dictionary.items():
        temp_val = value.get_department()
        dept_dict[temp_val] = {}

    #This puts values of salaries in all the depts
    for key, value in dictionary.items():
        temp_val = value.get_department()

        #this is our base case, when the dept does not have any previous salary
        if 'Max Salary' not in dept_dict[temp_val]:
            dept_dict[temp_val][max_salary] = -99999999999
            dept_dict[temp_val][min_salary] = 99999999999
            dept_dict[temp_val][sal_count] = 1
            dept_dict[temp_val][avg]= 0
            dept_dict[temp_val][total_sal]= 0
    
        else:
            dept_dict[temp_val][sal_count] += 1
    
        temp_salary = int(value.get_salary().replace(',',''))
        salary_avg += temp_salary
        salary_counter += 1

        max_sal = dept_dict[temp_val][max_salary]
        min_sal = dept_dict[temp_val][min_salary]
        if temp_salary > max_sal:
            dept_dict[temp_val][max_salary] = temp_salary

        if temp_salary < min_sal:
            dept_dict[temp_val][min_salary] = temp_salary

        dept_dict[temp_val][total_sal] += temp_salary
        dept_dict[temp_val][avg]= dept_dict[temp_val][total_sal]/ dept_dict[temp_val][sal_count]        
        
    # print the stats for the temp dictionary
    print()
    for key in dept_dict:
        print(key)
        for key2 in dept_dict[key]:
            #Don't print the Salary Count and Total Salary
            if key2 is not "Salary Count" and key2 != "Total Salary":
                print(key2,"{:,}".format(dept_dict[key][key2]))
        print()
    print()
    
def dispEmployees(dictionary):
    for key in dictionary:
        print(key, dictionary[key])
    print()
    
main()

