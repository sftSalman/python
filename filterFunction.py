# filter(function, iterator)
x = [1,2,3,4,5,6,7,7]
def greater(x):
   if x>2 :
      return x+1

numberFilter = filter(greater,x)
numberMap = map(greater,x)
print(list(numberFilter))
print(list(numberMap))