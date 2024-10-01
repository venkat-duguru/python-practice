#Give me an example for single inheritance
class Animal:
    def sound(self):
        return "some sound"


class Dog(Animal):
    def sound(self):
        return "Bark"


dog = Dog()
print(dog.sound())
