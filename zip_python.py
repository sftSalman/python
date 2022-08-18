name = ['salman','sami','rana']
roll = [1,3,4,2]
zip_map = zip(roll,name)
new = zip_map
print(list(new))

enum = enumerate(name)
zip_en= enumerate(zip(name,roll))
print(list(enum))
print(list(zip_en))