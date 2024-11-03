class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I called when an object is created")

    def change_password(self):
        self.password = "345"


xuv = Car()
xuv.password = "345"
