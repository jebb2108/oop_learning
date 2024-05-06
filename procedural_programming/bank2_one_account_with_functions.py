import random

""" Без ООП """
""" Банк 2 """
""" Единственный счет """

account_name = ''
account_balance = 0
account_password = ''


def new_account(name, balance, password):
    global account_name, account_balance, account_password
    account_name = name
    account_balance = balance
    account_password = password


def show():
    global account_name, account_balance, account_password
    print('           Name', account_name)
    print('           Balance:', account_balance)
    print('           Password:', account_password)
    print()


def get_balance(password: str) -> int or None:
    global account_name, account_balance, account_password
    if password != account_password:
        print('Incorrect password')
        return None
    return account_balance


def deposit(amount: int, password: str) -> int or None:
    global account_name, account_balance, account_password
    if amount < 0:
        print('You cannot deposit a negative number!')
        return None

    if password != account_password:
        print('Incorrect password')
        return None

    account_balance += amount
    return account_balance


def withdraw(amount: int, password: str) -> int or None:
    global account_name, account_balance, account_password
    if amount > account_balance:
        print('You don`t have enough money in your account')
        return None

    elif amount < 0:
        print('You cannot withdraw a negative amount!')
        return None

    if password != account_password:
        print('Incorrect password')
        return None

    account_balance -= amount
    return account_balance


new_account('Gabriel', 2000, 'qwerty')

while True:
    print()
    print('Press "b" to get the balance')
    print('Press "d" to make a deposit')
    print('Press "w" to make a withdrawal')
    print('Press "s" to show the account')
    print('Press "q" to quit')

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get Balance:')
        user_password = input('Please enter the password: ')
        the_balance = get_balance(user_password)
        if the_balance is not None:
            print('Your balance is:', the_balance)

    elif action == 'd':
        print('Deposit:')
        user_deposit_amount = int(input('Please enter amount to deposit: '))
        user_password = input('Please enter the password: ')

        new_balance = deposit(user_deposit_amount, user_password)
        if new_balance is not None:
            print('Your new balance is:', new_balance)

    elif action == 'w':
        print('Withdrawal:')
        user_withdrawal_amount = int(input('Please enter amount to withdraw: '))
        user_password = input('Please enter the password: ')

        new_balance = withdraw(user_withdrawal_amount, user_password)
        if new_balance is not None:
            print('Your new balance is:', new_balance)

    elif action == 's':
        print('Show:')
        show()

    elif action =='q':
        break

    else:
        print('Sorry, you typed in an unknown command')

print('Done')