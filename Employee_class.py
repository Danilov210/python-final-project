from Person_class import Person

class Employee(Person):
    def __init__(self, id, name, age, field_of_work, salary):
        super().__init__(id, name, age)
        self.salary = salary
        self.field_of_work = field_of_work
    
    def getFieldOfWork(self):
        return self.field_of_work
    
    def getSalary(self):
        return self.salary
    
    def getEmployeeString(self):
         return (self.getPersonString() + ", The field is " + self.getFieldOfWork() + ", the salary is " + str(self.getSalary()))
    
    def printMyselfString(self):
        print(self.getEmployeeString())
        
    def getMyselfString(self):
        return self.getEmployeeString()