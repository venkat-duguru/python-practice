#Give me an example for polymorphism
#Polymorphism is of 2 types
#i. overriding
#ii. overloading
class Bird:
    def fly(self):
        print("All birds can fly")


class Penguin(Bird):
    def fly(self):
        print("This bird cannot fly")


bird = Bird()
penguin = Penguin()
bird.fly()
penguin.fly()