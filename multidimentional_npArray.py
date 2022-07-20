import numpy as np

print(np.array(8))

# 2D array
ar2 = np.array([[1,2,3,4],[3,2,1,3]])
print(ar2)
ar3 = np.array([[[1,2,3],[3,4,2],[23,4,4]]])
print(ar3.shape)
arr4 = np.array([[[[1,2,3],[2,21,1],[23,32,3],[13,3,2],[1,2,3]]]])
print(arr4)
print(arr4.shape)
x = np.random.rand(4,3,3,2)
print(x)