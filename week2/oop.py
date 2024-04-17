# Understand OOP : classes/objects - inheritance - polymorphism - encapsulation

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount


account = Account("Armand")
print(account.owner)
account.set_balance(100)
print(account.get_balance())