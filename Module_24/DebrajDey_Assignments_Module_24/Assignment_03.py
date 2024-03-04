class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = int(balance.replace('$', ''))

    def Deposit(self, amount):
        self.balance += amount

    def Withdraw(self, amount):
        self.balance -= amount

    def display(self):
        print(f'Account Number :  {self.accountNumber}')
        print(f'Account Name :  {self.name}')
        print(f'Account Balance :  {self.balance} $')


new_account = BankAccount(2178514584, 'Tony', '$29800')
new_account.Deposit(100)
new_account.Withdraw(200)

new_account.display()
