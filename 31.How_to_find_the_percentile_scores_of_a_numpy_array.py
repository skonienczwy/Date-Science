#31 - Find the 5th and 95th percentile of iris's sepallength
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

print(np.percentile(sepallength, q=[5, 95]))