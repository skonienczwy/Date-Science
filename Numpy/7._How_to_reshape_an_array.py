#7 - Convert a 1D array to a 2D array with 2 rows
import numpy as np
#My Solution
array = np.arange(10).reshape(2,5)

print(array)

#Alternate Method 2#

array = np.arange(10).reshape(2,-1) # Setting to -1 automatically decides the number of cols
print(array)