import numpy as np
arr  = np.zeros(2,float)
arr2 = np.array([[np.zeros(5)],[np.zeros(5)]])
print(arr2)
print(type(arr2))
tu = (1,2,4,5,6,6,7)
arr3 = np.array(tu)
print(arr3)
print(type(arr3))
print(arr3.ndim)
print(arr2.ndim)

arr4 = np.array([1,2,3,4],ndmin=5)
arr5 = np.array([1,2,3,4,5,65])
print(arr5[0]+arr5[2])
arr2d= np.array([[1,2,3,4,5,6],[1,2,3,4,5,7]],dtype='f')
print(type(arr2d))
print(arr2d)
print(arr2d[1,5])
print(arr2d[1,2:5])
newarr= arr2d.astype('i')
print(newarr)
n2 = newarr.copy()
print(n2)
print(n2.view)
print(arr2d.shape)
print(arr2d.ndim)
n3 = arr2d.reshape(2,4)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)
