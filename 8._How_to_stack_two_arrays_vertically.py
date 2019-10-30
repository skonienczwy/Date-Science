#8- Stack arrays a and b vertically
import numpy as np

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
#My Solution
newArr = np.append(a, b , axis=0)
print(newArr)

#Alternate Method 2#
# print(np.concatenate([a, b], axis=0))

#Alternate Method 3#
# print(np.vstack([a, b]))
#Alternate Method 4#
# print(np.r_[a, b])