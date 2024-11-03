class Fruit:
    def taste(self):
        return "some taste"


class Banana(Fruit):
    def taste(self):
        return "Sweet"


fruit = Banana()
print(fruit.taste())

