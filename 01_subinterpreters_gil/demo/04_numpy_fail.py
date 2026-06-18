from concurrent import interpreters


import numpy as np

interpreter = interpreters.create()


def compute_mean(arr):
    return arr.mean()


data = np.random.rand(1_000_000)

interpreter.call(compute_mean, data)
