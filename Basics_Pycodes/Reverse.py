# Write a program to reverse a string without using built-in reverse functions.

text = "program"
reverse = "" #create a empty string 
for ch in text: #using for loop to the each string in that string
    reverse = ch + reverse #combining the each char from the reverse string
print("Reverse String:" , reverse)
