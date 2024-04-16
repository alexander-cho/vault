from account import Account

'''
Checking account
'''


class Checking(Account):
    
    def __init__(self, name, ssn, username, password) -> None:
        super().__init__(name, ssn, username, password)

    def deposit(self) -> None:
        return super().deposit()
    

    # check if total balance is under $45


    # 

    
    def __str__(self) -> str:
        pass