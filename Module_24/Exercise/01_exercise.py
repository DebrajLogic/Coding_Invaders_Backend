class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(self.balance)


my_account = BankAccount()

my_account.deposit(200)
my_account.withdraw(100)

my_account.show_balance()
