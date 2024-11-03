class Formula:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area_rectangle(self):
        return 1/2 * self.a * self.b


formula = Formula(4, 5)
print(formula.area_rectangle())