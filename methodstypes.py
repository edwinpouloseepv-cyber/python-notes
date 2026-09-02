# class Demo:
#     def show(self):
#         print("Instance method")
# d = Demo()
# d.show()

# class Demo:
#     @classmethod
#     def info(cls):
#         print("class method")
# Demo.info()


# class Demo:
#     @staticmethod
#     def utility():
#         print("static method")
# Demo.utility()

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount
b = BankAccount(1000)
b.deposit(500)
print("Balance:", b._balance)
b.withdraw(200)
print("Balance:", b._balance)