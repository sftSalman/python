x,y,z,n = map(int,input().split())
output = []
abc = []
for X in range(x+1):
    for Y in range(y+1):
        for Z in range(z+1):
            if X+Y+Z != n:
                abc = [X,Y,Z]
                output.append(abc)
print(output)