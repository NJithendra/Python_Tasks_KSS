#Random Number Analyzer

import random
nums = []
for i in range(10):
    nums.append(random.randint(1, 100))
even = 0
odd = 0
for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
unique = set(nums)
print("Numbers:", nums)
print("Even numbers:", even)
print("Odd numbers:", odd)
print("Unique numbers:", unique)
