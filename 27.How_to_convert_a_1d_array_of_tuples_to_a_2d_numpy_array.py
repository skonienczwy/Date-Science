#27 - Convert the 1D iris to 2D array iris_2d by omitting the species text field.

import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype='object')

# Method 1
# iris_2d = np.array([row.tolist()[:4] for row in iris_1d])
# print(iris_2d[:4])

# # Method 2
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
print(iris_2d[:4])