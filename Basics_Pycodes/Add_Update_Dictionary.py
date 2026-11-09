# Create a dictionary containing student names and marks. Add a new student, update an existing student's marks, and print all student details.

students = {
    "Rahul": 85,
    "Ram": 90,
    "Sita": 78
}
students["Lakshman"] = 95
students["Ram"] = 92
print(students)
for name, marks in students.items():#using loops through each key-value pair.
    print(name, marks)
