#9 -Stack the arrays a and b horizontally.
import numpy as np

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

#My Solution
newArr = np.append(a, b , axis=1)
print(newArr)
#
#Alternate Method 2#
# print(np.concatenate([a, b], axis=1))

# #Alternate Method 3#
# print(np.hstack([a, b]))
#
# #Alternate Method 4#
# print(np.c_[a, b])