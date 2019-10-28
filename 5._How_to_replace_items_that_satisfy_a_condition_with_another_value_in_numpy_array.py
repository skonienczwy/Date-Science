#5 - Replace all odd numbers in arr with -1
import numpy as np
arr = np.arange(10)
#My Solution


# for i in arr:
#     if  arr[i] % 2 != 0:
#         arr[i] = -1
#
# print(arr)

#Alternate Method 2#

arr[arr % 2 == 1] = -1
print(arr)