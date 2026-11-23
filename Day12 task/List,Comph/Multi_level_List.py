#Multi-Level List Transformation

data = [[1, 2, 3], [4, 5], [6]]
flat = [j for i in data for j in i]
even_squares = [i ** 2 for i in flat if i % 2 == 0]
print("Flattened:", flat)
print("Even Squares:", even_squares)
