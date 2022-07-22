import numpy as np
x= np.ones(3)
#print(x)
y = np.pad(x,pad_width=1)
#print(y)

x1 = np.ones((3,3))
#print(x1)
y1 = np.pad(x1,pad_width=2)
#print(y1)

x2 = np.ones((3,3,3))
#print(x2)
y2 = np.pad(x2,pad_width=1)
#print(y2)
y3 = np.pad(x1,((2,0),(2,0)),constant_values=2)
y3 = np.pad(x2,((2,0),(2,0),(0,0)),constant_values=0)
print(x2)
print('\n')
print(y3)





