# Write a program to calculate the factorial of a number using a loop.

a = int(input("Enter the number:"))
factorial = 1
for i in range(1, a+1):
    factorial = factorial * i
    print("Factorial =" , factorial)
    
