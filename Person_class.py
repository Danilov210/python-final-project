class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    
    def getID(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getPersonString(self):
         return "ID: " + str(self.id) + ", The person " + self.getName() + " is " + str(self.getAge()) + " years old"
    
    def printMyselfString(self):
        print(self.getPersonString())
        
    def getMyselfString(self):
        return self.getPersonString()