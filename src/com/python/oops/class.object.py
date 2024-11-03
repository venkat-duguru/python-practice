class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bird_info(self):
        print(f"Name : {self.name}, Age : {self.age}")


parrot1 = Parrot("Blu", 21)
parrot1.bird_info()
parrot2 = Parrot("Woo", 15)
parrot2.bird_info()

