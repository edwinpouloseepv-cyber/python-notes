class Customer:
    def __init__(self, name):
        self.customer_name = name
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
class Employee:
    def __init__(self, name):
        self.employee_name = name
class Loan:
    def __init__(self, loan_amount):
        self.amount = loan_amount
class Transaction:
    pass
customer = Customer()
bank_account = BankAccount()
employee = Employee()
loan = Loan()
transaction = Transaction()