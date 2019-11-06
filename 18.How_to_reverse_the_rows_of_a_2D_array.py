#18 - Reverse the rows of a 2D array arr
import numpy as np

arr = np.arange(9).reshape(3,3)
#My Solution
print(arr)
print(np.flip(arr,axis=0))

#Method 2
print(arr[::-1])