class Human:
    name = None
    age = None
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f"My name is {self.name} and I am {self.age} years old")


human = Human("Venkat", 33)
human.get_info()