class Person():
    def __init__(self,name,age, gender):
        self.name  = name
        self.age = age
        self.gender = gender

    def __str__(self):
        print(self.name,self.age,self.gender)

p = Person('Salman',23,'male')
p.__str__()