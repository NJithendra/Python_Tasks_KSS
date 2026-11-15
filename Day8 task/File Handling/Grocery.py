#Write a Python program that takes multiple grocery items and saves each item on a new line in grocery.txt.

f = open("grocery.txt", "w")
n = int(input("Enter number of items: "))
for i in range(n):
    item = input("Enter grocery item: ")
    f.write(item + "\n")
f.close()
print("Grocery items saved successfully.")
