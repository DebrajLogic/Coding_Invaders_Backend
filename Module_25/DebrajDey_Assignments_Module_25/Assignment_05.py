from abc import ABC, abstractmethod


class Bank(ABC):
    def bank_info(self):
        print('Welcome to the bank')

    @abstractmethod
    def interest(self, interest):
        pass


class SBI(Bank):
    def __init__(self):
        self.bank_interest = 5

    def interest(self):
        print(f'In sbi bank {self.bank_interest} rupees interest')


class Axix(Bank):
    def __init__(self):
        self.bank_interest = 8

    def interest(self):
        print(f'In axis bank {self.bank_interest} rupees interest')


sbi = SBI()
sbi.bank_info()
sbi.interest()


axis = Axix()
axis.bank_info()
axis.interest()
