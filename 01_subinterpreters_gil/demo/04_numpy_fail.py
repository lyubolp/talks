from concurrent.futures import InterpreterPoolExecutor

import numpy as np


def compute_mean(arr):
    return arr.mean()


data = np.random.rand(1_000_000)

with InterpreterPoolExecutor(max_workers=4) as executor:
    result = executor.submit(compute_mean, data).result()
    print(f"Mean: {result:.4f}")
