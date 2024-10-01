#write a program on encapsulation
class Employee:
    def __init__(self, name, id, salary, address):
        self.__name = name
        self.__id = id
        self.__salary = salary
        self.__address = address

    def get_data(self):
        return self.__name, self.__id, self.__salary, self.__address


emp = Employee("Venkatesh", 1, 10000, "Hyderabad")
emp.get_data()
print(emp.get_data())
