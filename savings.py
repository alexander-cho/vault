from account import Account

'''
Savings account
'''


class Savings(Account):

    def __init__(self, name, ssn, username, password) -> None:
        super().__init__(name, ssn, username, password)

    def deposit(self, amount) -> None:
        return super().deposit(amount)

    def __str__(self) -> str:
        pass
