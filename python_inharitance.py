class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def print_name(self):
        print(self.firstname , self.lastname)


x = Person('salman' , 'farshi')
x.print_name()

class Student(Person):
     pass

x2 = Student('Salman',"Farshi")
x2.print_name()