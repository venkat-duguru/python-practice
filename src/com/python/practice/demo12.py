#Give an example for Multi_inheitance
class Father:
    def height(self):
        return "Tall"


class Mother:
    def color(self):
        return "Fair"


class Child(Father, Mother):
    pass


child = Child()
print(child.height())
print(child.color())