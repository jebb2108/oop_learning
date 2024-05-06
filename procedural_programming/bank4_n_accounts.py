""" Без ООП """
""" Банк 4"""
""" Любое количество счетов - со списками """

account_name_list = []
account_balance_list = []
account_password_list = []


def new_account(name: str, balance: int, password: str):
    global account_name_list, account_balance_list, account_password_list
    account_name_list.append(name)
    account_balance_list.append(balance)
    account_password_list.append(password)


def show(account_num: int):  # all nums start with 0!
    global account_name_list, account_balance_list, account_password_list
    print('Account:', account_num)
    print('           Name', account_name_list[account_num])
    print('           Balance:', account_balance_list[account_num])
    print('           Password:', account_password_list[account_num])
    print()


def get_balance(account_num: int, password):
    global account_name_list, account_balance_list, account_password_list
    if password != account_password_list[account_num]:
        print('Incorrect password')
        return None
    return account_balance_list[account_num]


def deposit(account_num: int, amount: int, password: str) -> int or None:
    global account_name_list, account_balance_list, account_password_list
    if amount < 0:
        print('You cannot deposit a negative number!')
        return None

    if password != account_password_list[account_num]:
        print('Incorrect password')
        return None

    account_balance_list[account_num] += amount
    return account_balance_list[account_num]


def withdraw(account_num: int, amount: int, password: str) -> int or None:
    global account_name_list, account_balance_list, account_password_list
    if amount > account_balance_list[account_num]:
        print('You don`t have enough money in your account')
        return None

    elif amount < 0:
        print('You cannot withdraw a negative amount!')
        return None

    if password != account_password_list[account_num]:
        print('Incorrect password')
        return None

    account_balance_list[account_num] -= amount
    return account_balance_list[account_num]

print("Joe`s account number is:", len(account_name_list))
new_account('Joe', 2000, 'qwerty')

print("Mary`s account number is:", len(account_name_list))
new_account('Mary', 4000, 'soup')

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
        user_account_number = int(input('Please enter your account number: '))
        user_password = input('Please enter the password: ')
        the_balance = get_balance(user_account_number, user_password)
        if the_balance is not None:
            print('Your balance is:', the_balance)

    elif action == 'd':
        print('Deposit:')
        user_account_number = int(input('Please enter your account number: '))
        user_deposit_amount = int(input('Please enter amount to deposit: '))
        user_password = input('Please enter the password: ')

        new_balance = deposit(user_account_number, user_deposit_amount, user_password)
        if new_balance is not None:
            print('Your new balance is:', new_balance)

    elif action == 'w':
        print('Withdrawal:')
        user_account_number = int(input('Please enter your account number: '))
        user_withdrawal_amount = int(input('Please enter amount to withdraw: '))
        user_password = input('Please enter the password: ')

        new_balance = withdraw(user_account_number, user_withdrawal_amount, user_password)
        if new_balance is not None:
            print('Your new balance is:', new_balance)

    elif action == 's':
        print('Show:')
        show(int(input('Please enter your account number: ')))

    elif action =='q':
        break

    else:
        print('Sorry, you typed in an unknown command')

print('Done')