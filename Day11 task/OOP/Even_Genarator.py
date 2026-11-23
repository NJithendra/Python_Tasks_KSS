#Infinite Even Number Generator (Generators)

def even_numbers():
    n = 2
    while True:
        yield n
        n += 2
num = even_numbers()
N = int(input("Enter N: "))

for i in range(N):
    print(next(num))
