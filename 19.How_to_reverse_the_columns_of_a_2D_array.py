#19 - Reverse the columns of a 2D array arr
import numpy as np

arr = np.arange(9).reshape(3,3)

#My Solution
print(arr)
print(np.flip(arr,axis=1))

# #Method 2
# print(arr[:,::-1])


#Example to reverse specific rows

# arr = np.arange(24).reshape(6,4)
# a[1::2, :] = a[1::2, ::-1]
# 1 is the start, 2 every other row(row 2 is not included)