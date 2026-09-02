# class student:
#     name = "alice"  #public
# s = student()
# print(s.name)
# class example:
#     __private = 3  # private
# s = example()
# # print(s.__private)
# print(s._example__private)
# class Account:
#     _balance = 1000  #protected
# class SavingsAccount(Account):
#     def show_balance(self):
#         print(self._balance)
# acc = SavingsAccount()
# acc.show_balance()   #allowed
# print(acc._balance)  #allowed,but discouraged
