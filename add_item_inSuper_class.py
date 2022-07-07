class Person:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname

    def printname(self):
        print(self.first_name,self.last_name)

class Student(Person):
    def __init__(self,fname,lname,age):
        self.first_name = fname
        self.last_name = lname
        self.age = age
    def printname(self):
        print(self.first_name,self.last_name,self.age)


x = Person('salman','farshi')
x2 = Student('sami','salvi',34)
x.printname()
x2.printname()