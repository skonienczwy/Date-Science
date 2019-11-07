# 22 - Pretty print rand_arr by suppressing the scientific notation (like 1e10)
import numpy as np
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3

#My Solution
np.set_printoptions(suppress=True)
print(rand_arr)

#Method 2

# np.set_printoptions(suppress=False) #Reset printoptions to default
#
# np.random.seed(100)
# rand_arr = np.random.random([3,3])/1e3
#
# np.set_printoptions(suppress=True, precision=6)  # precision is optional
#
# print(rand_arr)

