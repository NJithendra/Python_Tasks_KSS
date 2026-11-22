#University Staff Management (Hierarchical Inheritance)

class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Professor(Staff):
    def display(self):
        print("Professor:", self.name, self.salary)
class LabAssistant(Staff):
    def display(self):
        print("Lab Assistant:", self.name, self.salary)
class Administrator(Staff):
    def display(self):
        print("Administrator:", self.name, self.salary)
p = Professor("Ravi", 60000)
l = LabAssistant("Kiran", 30000)
a = Administrator("Rahul", 40000)

p.display()
l.display()
a.display()
