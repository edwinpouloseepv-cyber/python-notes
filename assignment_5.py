choice = [1,2,3,4,5,6]
while choice !=6:
    balance = 0
    options = ["1.Create Account","2. Deposit","3. Withdraw","4. Check Balance","5. Transaction History","6. Exit"]
    for choice in options:
        print(choice)
    choice = int(input("enter any choice:"))
    def creat_account(name,account_type = "savings"):
        print("available accounts")
        ac = ["1.current account","2.fixed deposit account","3.recurring deposit account"]
        for type in ac:
            print(type)
        choice = int(input("select your account :"))
        if choice == 1:
            account_type = "current account"
            print("your account is selected as:",account_type)
        elif choice ==2:
            account_type = "fixed deposit account"
            print("your account is selected as:",account_type)
        elif choice ==3:
            account_type = "recurring deposit account"
            print("your account is selected as:",account_type)
        else:
            print("your account is selected as:",account_type)
        print("your account created successfuly")
        print("account holder name:",name)
        print("account type:",account_type)
        return name,account_type

    def Deposit_Amount( amount,balance):
        """This function adds amount to the balance"""
        balance += amount
        print(amount,"credited in your account")
        print("your account balance :",balance)
        return amount,balance
    def withdraw_amount(balance,withdraw):
        print("balance:",balance)
        balance -= withdraw
        print("you withdraw:",withdraw)
        print("your balance after withdraw:",balance) 
    def check_balance(balance):
        print("your account balance:",balance) 
    def transaction_history(*transaction):
        print("customer transaction history:",transaction)      
    if choice == 1:
        name,account_type = creat_account((input("enter your name:")))
    elif choice == 2:
        amount,balance = Deposit_Amount(float(input("enter amount:")))
    elif choice ==3:
        withdraw_amount(5000,1000)
    elif choice == 4:
        balance = check_balance(4000)
    elif choice == 5:
        transaction = transaction_history(1000,5000,100)
    else:
        break
            

