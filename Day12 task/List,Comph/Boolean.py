#Boolean Masking for Salary Analysis

import numpy as np
salary = np.array([25000, 40000, 15000, 50000, 30000])
result = salary[salary > 30000]
print("Salaries:", result)
print("Count:", len(result))
