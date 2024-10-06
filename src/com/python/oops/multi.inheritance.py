class Grandfather:
    def flat(self):
        return '1BHK'

class Father:
    def house(self):
        return "Individual house"

class Child(Grandfather, Father):
    pass


child = Child()
print(child.flat())
print(child.house())
