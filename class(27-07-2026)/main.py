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

# Creating An Object 

employee1 = Employee("Shrut", 12000, "Developer")
employee2 = Employee("Nitin", 25000, "Sales Manager")


print(employee2.position) #Sales Manager

employee1.checkin("12pm") #Shrut Checked in at 12pm
employee2.checkin("1 Pm") #Nitin Checked in at 1 Pm

developer1 = Developer("Baba", 12000, "Developer", "Python")

developer1.Working()
developer1.checkin("7am")


