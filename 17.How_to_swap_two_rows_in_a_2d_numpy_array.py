#17 - Swap rows 1 and 2 in the array arr:
import numpy as np

arr = np.arange(16).reshape(4,4)


print(arr)
print(arr[[3,2,1,0], :])



