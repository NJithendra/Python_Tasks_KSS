#Create a Python module named calculator.py that contains functions to perform:
# Addition
# Subtraction
# Multiplication
# Division


def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b
