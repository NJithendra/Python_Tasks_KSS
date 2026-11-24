#Student Marks Analysis

import numpy as np
import pandas as pd
arr = np.array([
    [80, 90],
    [70, 60],
    [85, 95]
])
df = pd.DataFrame(arr, columns=["Math", "Science"])
df["Total"] = df["Math"] + df["Science"]
print(df)
print("Highest Total:")
print(df.loc[df["Total"].idxmax()])
