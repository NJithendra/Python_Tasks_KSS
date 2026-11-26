#Data Cleaning + Visualization

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = np.array([100, np.nan, 200, 150, np.nan, 300])
s = pd.Series(data)
s = s.fillna(s.mean())
print("Cleaned Data:")
print(s)
average = s.mean()
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(s, marker='o')
plt.title("Cleaned Data Line Graph")
plt.xlabel("Index")
plt.ylabel("Values")
plt.grid(True)

plt.subplot(1, 2, 2)
filtered = s[s > average]
plt.bar(filtered.index, filtered.values)
plt.title("Values Above Average")
plt.xlabel("Index")
plt.ylabel("Values")
plt.tight_layout()
plt.show()
