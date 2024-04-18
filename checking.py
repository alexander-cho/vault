from datetime import datetime

from account import Account

'''
Checking account
'''


class Checking(Account):

    def __init__(self, name, ssn, username, password, total_balance) -> None:
        super().__init__(name, ssn, username, password, total_balance)

    def deposit(self, amount) -> None:
        return super().deposit(amount)

    def withdraw(self, amount) -> None:
        if self.total_balance - amount < 45:
            print('Your balance is less than $45, you will be charged a fee if this persists.')
        return super().withdraw(amount)

    def get_total_balance(self) -> None:
        return super().get_total_balance()
    
    def date_account_created(self) -> datetime:
        return super().date_account_created()

    def __str__(self) -> str:
        return super().__str__()
