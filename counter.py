from collections import Counter

counter = Counter(['a', 'a', 'b'])
print(counter)
# adding new counter value
counter['d']=4
print(counter)
# deleting value

del counter['d']
print(counter)

# elements which return only positive value

counter['n']=-1
print(counter)
print(counter.elements())
el= counter.elements()
for i in el:
    print(i)
# most common
mcn = counter.most_common(1)
print(mcn)
