class Account:
    def __init__(self, number, balance):
        self.__number = number
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = Account(123456789, 1000)
print(account.get_balance())

