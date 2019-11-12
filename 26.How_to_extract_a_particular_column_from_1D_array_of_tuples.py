#26 - Extract the text column species from the 1D iris imported in previous question.

import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=object)

species = np.array([row[4] for row in iris_1d])
print(species[:5])
