# Write a program to remove duplicate characters from a string.

s = input("Enter the String:")
output = ""
for ch in s:
    if ch not in output:
        output += ch
    print("Removing the duplicate characters:" , output)
    
