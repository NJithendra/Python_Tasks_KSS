#Create a Number Guessing Game where:
# The computer generates a random number between 1 and 50.
# The user gets 5 attempts.
# After every guess, calculate the absolute difference using math.fabs().
# Display how far the guess is from the correct number.

import random
import math
number = random.randint(1,50)
attempt = 5
print(" Number Guessing Game!")
print("Guess a number between 1 and 50")
for i in range(attempt):
    guess = int(input("Enter your guess:"))
    difference = math.fabs(number - guess)
    print("Difference:", difference)

    if guess == number:
        print("Your guess is correct")
    else:
        print("Your guess is not correct")
        print("The remaining attempt :" , attempt-i -1)

