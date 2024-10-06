class Animal:
    def eat(self):
        print("It can eat")

    def sleep(self):
        print("It will sleep")


class Dog(Animal):
    def bark(self):
        print("It can bark! Woof woof!!")


dog = Dog()
dog.eat()
dog.sleep()
dog.bark()