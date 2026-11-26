#Employee Management System

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
employees = {}

try:
    n = int(input("Enter number of employees: "))
    for i in range(n):
        name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        employees[name] = Employee(name, salary)
    with open("employees.txt", "w") as f:
        for name, emp in employees.items():
            f.write(name + " " + str(emp.salary) + "\n")
    for name, emp in employees.items():
        print("Name:", emp.name)
        print("Salary:", emp.salary)
except ValueError as e:
    print("Invalid input:", e)
