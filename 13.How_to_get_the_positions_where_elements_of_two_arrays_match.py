#13- Get the positions where elements of a and b match

import numpy as np
#My Solution
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

# print(np.where(np.in1d(a, b)))

#Alternate Method 2#
print(np.where(a == b))
