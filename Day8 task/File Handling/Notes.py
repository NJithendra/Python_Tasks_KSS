#Write a program to open notes.txt, read all its contents, and display them.

f = open("notes.txt", "r")
data = f.read()
print("my streak is near to 300:")
print(data)
f.close()
