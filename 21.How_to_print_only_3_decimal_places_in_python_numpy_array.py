#22 - Print or show only 3 decimal places of the numpy array rand_arr

import numpy as np

rand_arr = np.random.random((5,3))
np.set_printoptions(precision=3)
print(rand_arr)

