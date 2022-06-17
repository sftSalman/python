import numpy
a = numpy.matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
b = numpy.reshape(a, -1)
print(a)
print(b)
c=numpy.reshape(b,-1)
print(c)