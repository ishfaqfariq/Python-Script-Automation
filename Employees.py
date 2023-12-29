#Classes and Objects
class Employees:
    def __init__(self, name, department, role, salary, years_employed):
        self.name = name
        self.department = department
        self.role = role
        self.salary = salary
        self.years_employed = years_employed
# All classes have function called init fuciton and this is executed when the class 
# is being initiated, so we gonna use this init function to assign values
# object properties
        
# In summary, self is used to refer to the instance of the class, and __init__ is a special method used for initializing the attributes of the object when it is created. Together, they are fundamental in object-oriented programming in Python.

