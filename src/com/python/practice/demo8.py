#give an example for class and object
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def display_info(self):
        print(f'Model : {self.model}, Color : {self.color}')


car = Car("Hyundai", "Red")
car.display_info()
