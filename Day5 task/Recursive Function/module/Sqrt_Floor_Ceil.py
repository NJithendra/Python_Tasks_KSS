#Write a Python program using the math module to calculate and display the squareroot, floor value, and ceiling value of a number entered by the user.

import math
num = float(input("Enter a number:"))
sqrt = math.sqrt(num)
floor = math.floor(num)
ceil = math.ceil(num)

print("Square root:", sqrt)
print("Floor value:", floor)
print("Ceiling value:", ceil)
