#Advanced Simulation System
import random
import numpy as np
import pandas as pd
import math
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "Fail"
try:
    names = ["Jithendra", "Rahul", "Ravi", "Arun", "Kiran"]
    marks = np.random.randint(30, 101, 5)
    students = []
    for i in range(5):
        students.append(Student(names[i], int(marks[i])))
    data = []
    for s in students:
        data.append({
            "Name": s.name,
            "Marks": s.marks,
            "Grade": s.grade()
        })
    df = pd.DataFrame(data)
    print(df)
    average = math.ceil(np.mean(marks))
    print("Average Marks:", average)
    with open("exam_report.txt", "w") as f:
        f.write(df.to_string())
        f.write("\nAverage Marks: " + str(average))
    print("Report saved successfully")
except Exception as e:
    print("Error:", e)
