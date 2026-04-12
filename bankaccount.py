class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawn:", amount)
            else:
                print("Insufficient balance")
        else:
            print("Invalid amount")

    def check_balance(self):
        print("Balance:", self.balance)


account = BankAccount(101, 5000)

account.check_balance()
account.deposit(2000)
account.withdraw(1500)
account.check_balance()