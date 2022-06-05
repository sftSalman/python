from collections import Counter
counter = Counter({'a': 3, 'b': 3, 'c': 0})
# miscellaneous examples
print(sum(counter.values()))  # 6

print(list(counter))  # ['a', 'b', 'c']
print(set(counter))  # {'a', 'b', 'c'}
print(dict(counter))  # {'a': 3, 'b': 3, 'c': 0}
print(counter.items())  # dict_items([('a', 3), ('b', 3), ('c', 0)])

# remove 0 or negative count elements
counter = Counter(a=2, b=3, c=-1, d=0)
counter = +counter
print(counter)  # Counter({'b': 3, 'a': 2})

# clear all elements
counter.clear()
print(counter)  # Counter()