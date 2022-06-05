from collections import Counter
n = input()
sn = Counter(map(int,input().split()))
nn = input()
nnn = input(n)
earnings = 0
for i in range(nnn):
    size, price = map(int,input().split())
    if size in sn and sn[size]>0:
    sn[size] -= 1
    earnings = earnings + price
print(earnings)
