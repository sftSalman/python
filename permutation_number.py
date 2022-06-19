from itertools import  permutations
x = int(input())
y = int(input())
z = int(input())
n = int(input())

i = permutations(str(x),n)
j = permutations(str(y),n)
k = permutations(str(z),n)
for m in i:
    print(i)