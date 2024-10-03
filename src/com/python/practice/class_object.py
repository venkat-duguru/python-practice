class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'My name is {self.name}, and I am {self.age} years old')


p = Person("Venkat", 32)
p.info()