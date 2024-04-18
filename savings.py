from datetime import datetime

from account import Account

'''
Savings account
'''


class Savings(Account):

    def __init__(self, name, ssn, username, password, total_balance) -> None:
        super().__init__(name, ssn, username, password, total_balance)

    def deposit(self, amount) -> None:
        return super().deposit(amount)

    def withdraw(self, amount) -> None:
        if self.total_balance - amount < 500:
            print('Your balance is less than $500, you will be charged a fee if this persists.')
        return super().withdraw(amount)

    def get_total_balance(self) -> None:
        return super().get_total_balance()

    def date_account_created(self) -> datetime:
        return super().date_account_created()

    def __str__(self) -> str:
        pass
