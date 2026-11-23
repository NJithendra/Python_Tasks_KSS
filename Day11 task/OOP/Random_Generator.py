#Random Number Generator (Generators)

def generate(n):
    for i in range(1, n + 1):
        yield i
n = int(input("Enter N: "))
for num in generate(n):
    print(num)
