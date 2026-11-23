#Random Dataset Normalization

import numpy as np
arr = np.random.rand(8)
normalized = arr * 100
filtered = normalized[normalized > 50]
sorted_arr = np.sort(filtered)

print("Random Values:", arr)
print("Normalized:", normalized)
print("Filtered:", filtered)
print("Sorted:", sorted_arr)
