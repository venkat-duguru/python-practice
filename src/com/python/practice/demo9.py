#Give me an example for class and method
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


circle = Circle(4)
print(circle.area())
