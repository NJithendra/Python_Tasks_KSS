#Write a Python program that generates 20 random numbers between 1 and 200 using the random module and store them in a list. Then using the math module, compute and display:
#Maximum value
#Minimum value
#Square root of the maximum number
#Logarithm of the minimum number

import random
import math

number = []
for i in range(1,10):
    num = random.randint(1,200)
    number.append(num)
print("Random number:" ,number)

maximum = max(number)
minimum = min(number)
sqrt = math.sqrt(maximum)
log = math.log(minimum)

print("The maximum number :" , maximum)
print("The minimum number :", minimum)
print("The Square root is :", sqrt)
print("The logarith is :", log)
