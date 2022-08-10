from array import *
T = [[1,2,3,4],[1,2,3,4]]
print(T)
for i in T :
    for j in i:
        print(j,end=' ')
    print()

T.insert(0,[2,2,2,2])
print(T)
del T[0]

print(T)