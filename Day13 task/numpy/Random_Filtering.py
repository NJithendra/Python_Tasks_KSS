#Random Data & Filtering

import numpy as np
nums = np.random.randint(1, 100, 10)
result = nums[nums % 5 == 0]
result = np.sort(result)
print("Random Numbers:", nums)
print("Filtered and Sorted:", result)
