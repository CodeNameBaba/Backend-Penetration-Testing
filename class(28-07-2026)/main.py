# ==========================================
# PART 1: THE OLD WAY (Procedural Programming)
# ==========================================
# Without OOP, we store data in simple lists.
# The problem? We have to memorize that index 0 is the name and index 1 is the salary.
# This gets very confusing and messy when building large applications!

emp1 = ["Shrut", 12000]
emp2 = ["Nitin", 15000]

# We have to use numbers to get our data. Not very readable!
# print(emp1[0]) # Prints "Shrut"
# print(emp2[1]) # Prints 15000


# ==========================================
# PART 2: THE OOP WAY (Parent Class)
# ==========================================
# OOP lets us create a "blueprint" (a Class) for real-world things.
# Here, we create an 'Employee' blueprint.

class Employee:
    # 1. THE CONSTRUCTOR (__init__)
    # Think of this as the "birth" of an object. Whenever we create a new employee,
    # this setup function runs automatically to assign their specific details.
    def __init__(self, name, salary):
        # 'self' means "THIS specific object".
        # We are saying: "This specific employee's name = the name provided"
        self.name = name
        self.salary = salary

    # 2. A METHOD (An action the object can do)
    # Functions that live inside a class are called "methods".
    def kaam_karao(self):
        print(f"{self.name} is working.")


# Now let's use the blueprint to create actual objects (instances)!
employee1 = Employee("Shrut", 12000)
employee2 = Employee("Nitin", 12000)
emp3 = Employee("Kazim", 15000)

# We can access their data cleanly using a "dot" (.). No more confusing numbers!
# print(employee2.salary, employee2.name)

# We can make them perform actions using their methods!
# employee1.kaam_karao()
# emp3.kaam_karao()


# ==========================================
# PART 3: INHERITANCE (Child Classes)
# ==========================================
# What if we have specific TYPES of employees? We don't want to rewrite all the code!
# We can create "Child Classes" that inherit basic traits from the "Parent Class" (Employee).

class Developer(Employee):
    # Developers have a name and salary, but also a programming language!
    def __init__(self, name, salary, language):
        # super() calls the Parent Class (Employee).
        # We tell the parent: "Hey, handle the name and salary setup for me!"
        super().__init__(name, salary)
        # Then, we handle the new, specific detail ourselves:
        self.language = language

    # The Developer has a specialized way of working. 
    # This overrides the basic "kaam_karao" concept.
    def working(self):
        print(f"{self.name} is writing code in {self.language}.")


class Salesman(Employee):
    # Salesmen have a name and salary, but also a client they are calling!
    def __init__(self, name, salary, calling):
        # Let the Employee parent handle name and salary
        super().__init__(name, salary)
        # Handle the specific salesman trait
        self.calling = calling

    # The Salesman has their own specialized way of working.
    def working(self):
        print(f"{self.name} is calling {self.calling}.")


# ==========================================
# PART 4: PUTTING IT ALL TOGETHER
# ==========================================

# Create a Salesman object
salesman1 = Salesman("Kazim", 3000, "Baba")

# Create a Developer object
developer1 = Developer("Shahwar", 6000, "Java")

# Let's see them work! Because they are different objects,
# they know exactly how to do their own specific jobs using the dot (.)
salesman1.working()
developer1.working()
