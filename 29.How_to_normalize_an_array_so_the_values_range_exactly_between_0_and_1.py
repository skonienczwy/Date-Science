#29 - Create a normalized form of iris's sepallength whose values range exactly between 0 and 1
# so that the minimum has value 0 and maximum has value 1

import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])


# smax, smin = sepallength.max(), sepallength.min()
# s = (sepallength - smin)/(smax - smin)
#
# print(s)

smin = sepallength.min()
s = (sepallength - smin)/sepallength.ptp()
print(s)