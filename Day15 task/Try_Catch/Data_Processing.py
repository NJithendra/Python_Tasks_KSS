#Smart Data Processing Pipeline

import numpy as np
import pandas as pd
import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end - start)
    return wrapper
def read_numbers():
    with open("numbers.txt", "r") as f:
        for line in f:
            try:
                yield float(line.strip())
            except ValueError:
                print("Invalid data:", line.strip())
def process_data():
    try:
        nums = list(read_numbers())

        if len(nums) == 0:
            print("No valid numbers found")
            return

        arr = np.array(nums)

        mean = np.mean(arr)
        std = np.std(arr)

        df = pd.DataFrame({
            "Mean": [mean],
            "Standard Deviation": [std]
        })
        print(df)
    except FileNotFoundError:
        print("File not found")
process_data()
