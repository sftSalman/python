import numpy as np
arr = np.array([2,3,4,5,6,5])
x = np.where(arr==5)
y = np.searchsorted(arr,3)
print(y)