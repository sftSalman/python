import numpy as np
arr1=np.array([1,2,3,4,5])
arr2 = np.array([3,4,5,6,7])
arr = np.stack((arr1,arr2),axis=1)
arrh = np.hstack((arr1,arr2))
arrn = np.concatenate((arr1,arr2))
arrv = np.vstack((arr1,arr2))
print(arr)
print(arrh)
print(arrn)
print(arrv)
