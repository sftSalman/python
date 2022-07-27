x = 5
lambda x,y:x+3
x = lambda a,b: a*b
print(x(2,2))


# map(fucntion,iterable(s)

def myfun(n):
    return len(n)
x=map(myfun,('apple', 'banana', 'cherry'))
print(tuple(x))

