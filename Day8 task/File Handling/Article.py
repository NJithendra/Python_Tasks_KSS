#Write a Python program to count the number of words, lines, and characters in article.txt

f = open("article.txt", "r")
data = f.read()
words = data.split()
lines = data.splitlines()
characters = len(data)

print("Number of Words:", len(words))
print("Number of Lines:", len(lines))
print("Number of Characters:", characters)
f.close()
