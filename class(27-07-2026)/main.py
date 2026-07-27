# Object Oriented Programming With Python...


# 1 Procedural Programming...


emp1  = ["Shrut", 12000, "Developer"]
emp2  = ["Nitin", 123000]
emp3  = "Baba"

print(emp1[0])




# 2 Object Oriented Programming...

#Parent Class
class Employee:
    def __init__ (self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position


    def checkin(self, time):
        self.time = time
        print(f"{self.name} checked in at {self.time}")



#Child Class
class Developer(Employee):
    def __init__(self, name, salary, position, language):
        super().__init__(name, salary, position)

        self.language = language

    def Working(self):
        print(f"{self.name} is writting code in {self.language}")


class Salesman(Employee):
    def __init__(self, name, salary, position, calling):
        super().__init__(name, salary, position)
        self.calling = calling

    def Working(self):
        print(f"{self.name} is calling {self.calling}")


# Creating An Object 

employee1 = Employee("Shrut", 12000, "Developer")
employee2 = Employee("Nitin", 25000, "Sales Manager")


print(employee2.position) #Sales Manager

employee1.checkin("12pm") #Shrut Checked in at 12pm
employee2.checkin("1 Pm") #Nitin Checked in at 1 Pm

#Creating An Instance of the child Class
developer1 = Developer("Baba", 12000, "Developer", "Python")

#Method of child Class
developer1.Working()

#Method of parent class being inherited by child
developer1.checkin("7am")

# employee1.Working()     --This Will Give An Error As The Parent Class Cannot Use A Method Initialised By A Child Class


# Method OF Another Child Class
salesman1 = Salesman("Nitin", 10000, "Salesman", "Kazim")

salesman1.Working()