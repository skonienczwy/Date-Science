#4 - Extract all odd numbers from arr
import  numpy as np
arr = np.arange(10)
#My Solution

# arr2 = []
# for i in arr:
#
#     if arr[i]%2 !=0:
#        arr2.append(i)
# print(arr2)


#Alternate Method 2#

print(arr[arr % 2 == 1])
