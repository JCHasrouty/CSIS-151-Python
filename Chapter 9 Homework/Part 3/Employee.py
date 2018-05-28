class Employee():

##    def __setitem__(self, key, item):
##        self.__dict__[key] = item
##
##    def __getitem__(self, key):
##        return self.__dict__[key]
##
##    def __delitem__(self, key):
##        del self.__dict__[key]
##
##    def clear(self):
##        return self.__dict__.clear()
##
##    def copy(self):
##        return self.__dict__.copy()
##
##    def has_key(self, k):
##        return k in self.__dict__
##
##    def update(self, *args, **kwargs):
##        return self.__dict__.update(*args, **kwargs)
##
##    def keys(self):
##        return self.__dict__.keys()
##
##    def values(self):
##        return self.__dict__.values()
##
##    def items(self):
##        return self.__dict__.items()
##
##    def pop(self, *args):
##        return self.__dict__.pop(*args)
##
##    def __cmp__(self, dict_):
##        return self.__cmp__(self.__dict__, dict_)
##
##    def __contains__(self, item):
##        return item in self.__dict__
##
##    def __iter__(self):
##        return iter(self.__dict__)
##

    def __init__(self, emp_ID,department,job_title, salary):
        self.emp_ID = emp_ID
        self.department = department
        self.job_title = job_title
        self.salary = salary

    # Mutators
    def set_emp_name(self,emp_name):
        self.emp_name = emp_name
    
    def set_emp_ID(self,emp_ID):
        self.emp_ID = emp_ID

    def set_department(self,department):
        self.department = department

    def set_job_title(self,job_title):
        self.job_title = job_title

    def set_salary(self,salary):
        self.salary = salary

    #Accessor Methods
    def get_emp_name(self):
        return self.emp_name
    
    def get_emp_ID(self):
        return self.emp_ID

    def get_department(self):
        return self.department

    def get_job_title(self):
        return self.job_title

    def get_salary(self):
        return self.salary

    def get_data(self):
        print(self.emp_ID,self.department,self.job_title, self.salary)

    def __str__(self):
        return ("ID# " + self.emp_ID + " Department: " + self.department + " Job Title: " + self.job_title + " Salary: " + self.salary)
