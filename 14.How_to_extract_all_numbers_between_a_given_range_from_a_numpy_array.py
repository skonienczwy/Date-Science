#14 - Get all items between 5 and 10 from a.

import numpy as np

a = np.array([2, 6, 1, 9, 10, 3, 27])
#Method 1
# index = np.where((a >= 5) & (a <= 10))
# print(a[index])

#Method 2
# index = np.where(np.logical_and(a>=5, a<=10))
# print(a[index])

#Method 3
print(a[(a >= 5) & (a <= 10)])