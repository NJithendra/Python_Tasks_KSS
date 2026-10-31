# Write a program that searches for a number in a list and breaks the loop when found.

num = [10,22,30,45,52]
search = 22
for i in num:
    if i == search:
        print("Found Number:" , i)
        break
