class myClass :
    x = 5
m = myClass()
print(m.x)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


p = Person("salman",23)
print(p)

class New:
    def new(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return New(self.name,self.age)
#n = New('salman',23)
n = New()
s=n.new('Salman',23)
print(n.name)

