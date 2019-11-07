#20 - Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.

import numpy as np

#My Solution
# print(np.random.randint(5,high=10,size=15).reshape(5,3))
#as palavras high e size sao opicionais,pode se colocar os valores direto (5,10,15)

#Method 2

# arr = np.arange(9).reshape(3,3)
# rand_arr = np.random.randint(low=5, high=10, size=(5,3)) + np.random.random((5,3))
# print(rand_arr)

#Method 3

rand_arr = np.random.uniform(5,10, size=(5,3))
print(rand_arr)



