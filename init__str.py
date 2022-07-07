class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'Person({self.first_name},{self.last_name},{self.age})'
    def __repr__(self):
        return  f'({self.first_name},{self.last_name},{self.age})'

class Student(Person):
    def __init__(self,first_name,last_name , age,year ):
       # Person.__init__(self, first_name,last_name,age)
        super().__init__(first_name,last_name,age)
        self.new = year
    def __repr__(self):
        return  f'({self.age})'




person = Person('salman','farshi',24)
person2 = Student('salman','farshi',24,2022)
print(person)
print(repr(person))
print(person2)
print(Student)