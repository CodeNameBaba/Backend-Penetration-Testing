# Class Object Oriented Programming Explained Again 

# Procedural Programming 

# emp1 = ["Shrut", 12000]
# emp2 = ["Nitin", 15000]

# print(emp1[0])
# print(emp2[1])


# Object Oriented Programming 

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def kaam_karao(self):
        print(f"{self.name} is working ")




employee1 = Employee("Shrut", 12000)

# print(employee1.name)


employee2 = Employee("Nitin", 12000)

emp3 = Employee("Kazim", 15000)

# print(employee2.salary , employee2.name)


# employee1.kaam_karao()
# emp3.kaam_karao()


#Child Class Of Employee
class Developer(Employee):

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def working(self):
        print(f"{self.name} is writting code in {self.language}")




# developer1.working()
# developer1.kaam_karao()


class Salesman(Employee):
    def __init__(self, name, salary, calling):
        super().__init__(name,salary)
        self.calling = calling

    def working(self):
        print(f"{self.name} is calling {self.calling}")


salesman1 = Salesman("Kazim", 3000, "Baba")
developer1 = Developer("Shahwar", 6000, "Java")


salesman1.working()
developer1.working()