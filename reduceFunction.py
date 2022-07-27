from fractions import Fraction
def product(fracs):
    t = Fraction(lambda x,y: x*y,fracs)
    return t.numerator,t.denominator


fracs = []
for _ in range(int(input())):
    fracs.append(Fraction(*map(int, input().split())))
result = product(fracs)
print(*result)