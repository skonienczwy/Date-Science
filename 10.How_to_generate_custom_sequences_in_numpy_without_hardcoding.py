#10 - Create the following pattern without hardcoding.
# Use only numpy functions and the below input array a.

import numpy as np
a = np.array([1,2,3])
array = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print(array)



