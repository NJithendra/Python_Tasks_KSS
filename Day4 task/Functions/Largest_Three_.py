# Write a Python program with a function that returns the largest of three numbers.

def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
print("Largest number:", largest(10, 25, 15))
