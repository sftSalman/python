def solve(s):
    s1 = s.split(' ')
    s2 = ''
    for i in range(0, len(s1)):
        s2 = s2 + ' ' + s1[i].capitalize()
    return (s2)

print(solve(input()))