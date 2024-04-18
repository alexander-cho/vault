
def main():
    checking1 = Checking('alex', '123456', '<EMAIL>', '123456', total_balance=0)
    print(f'Welcome, {checking1.name}, your account was created on {checking1.date_account_created()}')
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


if __name__ == '__main__':
    main()
