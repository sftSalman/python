
# simple slicing
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
print(data[:])
print(data[2:])

# simple slicing
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
print(data[-2:])
# split input and output
from numpy import array
# define array
data = array([[11, 22, 33],
		[44, 55, 66],
		[77, 88, 99]])
# separate data
X, y = data[:, :-1], data[:, -1]
print(X)
print(y)
#https://towardsdatascience.com/advanced-numpy-array-indexing-made-easy-fc49fdaef367