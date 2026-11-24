#Reshape & Row Averages

import numpy as np
data = np.arange(1, 13)
matrix = data.reshape(3, 4)
avg = np.mean(matrix, axis=1)
print("Matrix:")
print(matrix)
print("Row Averages:", avg)
