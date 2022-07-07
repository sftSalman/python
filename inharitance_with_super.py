class Person:
    def __init__(self, name , age , gender , address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def print_person(self):
        print(self.name,self.age,self.gender,self.address)

p = Person("salman",23,'male','pabna')
p.print_person()