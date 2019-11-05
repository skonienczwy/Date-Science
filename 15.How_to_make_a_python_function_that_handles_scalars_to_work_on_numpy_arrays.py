#15 - Convert the function maxx that works on two scalars, to work on two arrays.
import numpy as np

#My Solution
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y


# print(np.maximum(a,b))

#Method 2

pair_max = np.vectorize(maxx, otypes=[float])
print(pair_max(a,b))