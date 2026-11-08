# Write a function that takes a string as input and returns the number of vowels.

def count_vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiou":
            count = count + 1
    return count
text = "Hello World"
print("Number of vowels:", count_vowels(text))
