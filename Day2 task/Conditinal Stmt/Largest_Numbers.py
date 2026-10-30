# Write a program to find the largest of three numbers using if-elif-else.

a = int(input("Enter the First number"))
b = int(input("Enter the Second number"))
c = int(input("Enter the Third number"))

if a >= c and a >= b:
    print("Largest:" , a)
elif b >= c and b >= a:
    print("Largest:" , b)
else:
    print("Largest:" , c)


