# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# c = a / b
# print("Result:", c)

# print("start")
# print(10 / 0)
# print("end")

# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     print("cannot divide by zero")
# except Exception as e:
#     print("Unexpected error:", e)
# else:
#     print("Result:", result)
# finally:
#     print("cleanup complete")

# def divide(a, b):
#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         print("error occurred inside divide ()")
#         raise
# try:
#     result = divide(10, 0)
#     print("Result:", result)
# except ZeroDivisionError:
#     print("caller the error")

# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except Exception :
#     print("General error")

# try:
#     val = int(input("Enter a number: "))
# except (ValueError, TypeError) as e:
#     print("invalid input:", e)

# try:
#     f = open("data.txt","r")

#     try:
#         data = f.read()
#         number = int(data)

#     except ValueError:
#         print("file does not contain a valid integer")
#     finally:
#         f.close()
# except FileNotFoundError:
#     print("file not f

class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds in the account")
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")
b = BankAccount(1000)
b.withdraw(500)  

