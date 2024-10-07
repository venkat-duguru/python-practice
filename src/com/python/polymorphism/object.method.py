class Calc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def floor_div(self):
        return self.a // self.b


calc = Calc(3, 4)
output = calc.sum()
print(output)
print(calc.sub())
print(calc.mul())
print(calc.div())
print(calc.floor_div())
