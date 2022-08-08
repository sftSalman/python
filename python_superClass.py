class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old.")


# Subclass 1.
class Student(Person):
    def __init__(self, name, age, graduation_year):
        super().__init__()
        self.graduation_year = graduation_year

    def info(self):
        # Call the Person classes introduce() method to introduce this Student.
        super().introduce()
        print(f"{self.name} will graduate in {self.graduation_year}")


alice = Student("Alice", 30, 2023)
alice.info()