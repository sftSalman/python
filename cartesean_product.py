from itertools import product
def solve(l1, l2):
  return list(product(l1, l2))

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
pro= solve(l1, l2)
for item in pro:
   print(item,end=' ')