from collections import Counter
c = Counter('abaadefs')
print(c)
s = Counter('a')
c.subtract(s)
print(c)
n = Counter('a')
c.update(n)
print(c)
