#32 - Insert np.nan values at 20 random positions in iris_2d dataset

import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')

# Method 1
i, j = np.where(iris_2d)

# i, j contain the row numbers and column numbers of 600 elements of iris_x
np.random.seed(100)
iris_2d[np.random.choice((i), 20), np.random.choice((j), 20)] = np.nan

# Method 2
# np.random.seed(100)
# iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
print(iris_2d[:10])
