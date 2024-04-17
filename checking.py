from account import Account

'''
Checking account
'''


class Checking(Account):
    
    def __init__(self, name, ssn, username, password) -> None:
        super().__init__(name, ssn, username, password)

    def deposit(self, amount) -> None:
        return super().deposit(amount)

    def withdraw(self, amount) -> None:
        return super().withdraw(amount)

    def get_total_balance(self) -> None:
        return super().get_total_balance()

    # check if total balance is under $45

    #

    def __str__(self) -> str:
        pass


if __name__ == '__main__':
    checking1 = Checking('alex', '123456', '<EMAIL>', '123456')
    while True:
        user_input = input('Enter your choice: ')
        if user_input == 'd':
            deposit_amount = float(input('Enter your deposit amount: '))
            checking1.deposit(deposit_amount)
        elif user_input == 'w':
            withdraw_amount = float(input('Enter your withdraw amount: '))
            checking1.withdraw(withdraw_amount)
        elif user_input == 't':
            checking1.get_total_balance()
        elif user_input == 'q':
            break
        else:
            print('Invalid input, try again')
