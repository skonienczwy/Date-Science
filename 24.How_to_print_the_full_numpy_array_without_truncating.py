#24 - Print the full numpy array a without truncating.


import numpy as np

np.set_printoptions(threshold=6)
a = np.arange(15)

np.set_printoptions(threshold=np.inf)
print(a)