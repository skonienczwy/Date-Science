#16 - Swap columns 1 and 2 in the array arr.

import numpy as np

arr = np.arange(9).reshape(3,3)
print(arr)
print(arr[:, [1,0,2]])

