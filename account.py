"""
Account base class
"""

from datetime import datetime


class Account:

    def __init__(self, name, ssn, username, password, total_balance=None) -> None:
        self.name = name
        self.ssn = ssn
        self.username = username
        self.password = password
        self.date_created = datetime.now()
        if total_balance is None:
            self.total_balance = 0
        else:
            self.total_balance = float(total_balance)

    def deposit(self, amount) -> None:
        if amount > 3000:
            print('You cannot deposit more than $3,000 at a time.')
        else:
            self.total_balance += amount
            print(f'You have deposited ${amount}')

    def withdraw(self, amount) -> None:
        if amount > self.total_balance:
            print('Your account balance is insufficient for that.')
        elif amount > 3000:
            print('You cannot withdraw more than $3,000 at a time.')
        else:
            self.total_balance -= amount
            print(f'You have withdrawn ${amount}')

    def get_total_balance(self) -> None:
        print(self.total_balance)
        # return self.total_balance

    def date_account_created(self) -> datetime:
        return self.date_created

    def __str__(self) -> str:
        return f'This is the account of {self.name}'
