#6- Replace all odd numbers in arr with -1 without changing arr

import numpy as np
#My solution
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# arr[arr % 2 != 0] = -1
# print(arr)
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(arr)


#Alternate Method 2#
out = np.where(arr % 2 != 0, -1, arr)
print(out)
print(arr)