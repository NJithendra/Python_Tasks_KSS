#Student Score Processor

import math
students = [("Jithendra", 85), ("Rahul", 45), ("Ravi", 65), ("Arun", 40)]
data = dict(students)
total = 0
count = 0
for name, marks in data.items():
    if marks > 50:
        print(name, marks)
    total += marks
    count += 1
average = math.ceil(total / count)
with open("student_scores.txt", "w") as f:
    f.write(str(data))
    f.write("\nAverage: " + str(average))
print("Average:", average)
print("Data saved successfully")
