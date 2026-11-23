# Student Information System (Class & Object)

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)

s1 = Student("Jithendra", 101, 90)
s2 = Student("Rahul", 102, 85)
s3 = Student("Kiran", 103, 95)

s1.display()
s2.display()
s3.display()
