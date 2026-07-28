# ==========================================
# PART 1: PROCEDURAL PROGRAMMING (The Messy Way)
# ==========================================
# Look at how inconsistent this is! 
# emp1 has 3 items, emp2 is missing a position, and emp3 is just a string.
# If a program tries to find emp3's salary, it will crash. 
# This is why we need OOP to enforce rules and structure.

emp1 = ["Shrut", 12000, "Developer"]
emp2 = ["Nitin", 123000]
emp3 = "Baba"

# We have to guess what index 0 means. Not great for teamwork!
print(emp1[0])


# ==========================================
# PART 2: OOP - THE PARENT CLASS (The Blueprint)
# ==========================================
# We create a strict template. EVERY employee MUST have a name, salary, and position.

class Employee:
    # 1. THE CONSTRUCTOR (Setting up the employee)
    def __init__ (self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    # 2. A BEHAVIOR (What the employee can do)
    def checkin(self, time):
        # We can even create new object variables later, like 'self.time'
        self.time = time
        print(f"{self.name} checked in at {self.time}")


# Let's create our base Employee objects
employee1 = Employee("Shrut", 12000, "Developer")
employee2 = Employee("Nitin", 25000, "Sales Manager")

print(employee2.position) # Outputs: Sales Manager

# Let's make them perform an action
employee1.checkin("12pm") # Shrut checked in at 12pm
employee2.checkin("1 Pm") # Nitin checked in at 1 Pm


# ==========================================
# PART 3: OOP - CHILD CLASSES (Specialized Blueprints)
# ==========================================
# Developers and Salesmen are just specific types of Employees.
# They share the basic traits (name, salary) but have unique skills.

class Developer(Employee):
    def __init__(self, name, salary, position, language):
        # 'super()' passes the basic details up to the Employee parent to handle
        super().__init__(name, salary, position)
        # We handle the specialized detail here
        self.language = language

    # A specialized method only for Developers
    def Working(self):
        print(f"{self.name} is writing code in {self.language}")


class Salesman(Employee):
    def __init__(self, name, salary, position, calling):
        super().__init__(name, salary, position)
        self.calling = calling

    # A specialized method only for Salesmen
    def Working(self):
        print(f"{self.name} is calling {self.calling}")


# ==========================================
# PART 4: PUTTING INHERITANCE TO THE TEST
# ==========================================

# 1. Create a Developer child object
developer1 = Developer("Baba", 12000, "Developer", "Python")

# 2. The child can use its OWN method
developer1.Working() 

# 3. The child can use its PARENT'S method! (This is the magic of inheritance)
developer1.checkin("7am") 

# Create a Salesman child object
salesman1 = Salesman("Nitin", 10000, "Salesman", "Kazim")
salesman1.Working()


# ==========================================
# PART 5: THE GOLDEN RULE OF INHERITANCE
# ==========================================
# Uncommenting the line below will crash the program. WHY?
# employee1.Working()     

# THE LESSON: 
# employee1 is a PARENT (Employee). 
# The Working() method was invented by the CHILDREN (Developer/Salesman).
# Traits flow DOWN from parent to child, never UP from child to parent!
