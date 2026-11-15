#Write a Python program that takes a student name as input, appends it to attendance.txt, and displays the file contents.

name = input("Enter student name: ")
f = open("att.txt", "a")
f.write(name + "\n")
f.close()

f = open("att.txt", "r")
print("Attendance Records:")
print(f.read())
f.close()
