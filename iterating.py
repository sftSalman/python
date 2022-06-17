import numpy as np
arr = np.array([[[np.random.random(5)],[np.zeros(5)],[np.ones(5)]]])
print(arr)
for x in np.nditer(arr):
    print(x)
arr2 = np.array([1, 2, 3])

for x in np.nditer(arr2, flags=['buffered'], op_dtypes=['S']):
  print(x)
for idx, x in np.ndenumerate(arr2):
    print(idx,x)