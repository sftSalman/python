import numpy as np

a = np.zeros((9))

print(len(a))

for i in range  (len(a)):
    a[i]= a[i]+1
    print(a)

print('thid is  new array', a)
