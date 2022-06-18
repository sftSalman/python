from itertools import permutations
s,n = input().upper().split()
p = permutations(s,int(n))

new =[]
for i in p:
   new.append(''.join(i))
print('\n'.join(sorted(new)))

