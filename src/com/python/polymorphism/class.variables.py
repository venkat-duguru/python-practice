class Person:

    name = "Venkat"
    age = 32

    def walk(self):
        a = 10
        print("I am a Method")
        print(f"Hi {self.name}, is your age {self.age}")


person = Person()
person.walk()
