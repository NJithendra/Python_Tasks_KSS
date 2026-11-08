# Write a program to check whether a string is a palindrome.

str = input("Enter the string:")
if str == str[::-1]:
    print("It is the palindrome")
else:
    print("It is not palindrome")
    
