from package import Math_Operator
from package import String_Operator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", math_operations.addition(a, b))
print("Multiplication:", math_operations.multiplication(a, b))

text = input("Enter a string: ")
print("Uppercase:", string_operations.uppercase(text))
print("Character count:", string_operations.count_characters(text))
