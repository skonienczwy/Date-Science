#25 - Import the iris dataset keeping the text intact.

import numpy as np

# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
url = 'iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

print(iris)