""" Без ООП """
""" Банк 5 """
""" Любое количество счетов - со списком словарей """

account_list = []


def new_account(a_name, a_balance, a_password):
    global account_list
    new_account_dict = {'name': a_name, 'balance': a_balance,
                        'password': a_password}
    account_list.append(new_account_dict)


def show(account_num):
    global account_list
    print('Account:', account_num)
    this_account_dict = account_list[account_num]
    print('           Name', this_account_dict['name'])
    print('           Balance:', this_account_dict['balance'])
    print('           Password:', this_account_dict['password'])
    print()


def get_balance(account_num, password):
    global account_list
    this_account_dict = account_list[account_num]
    if password != this_account_dict['password']:
        print('Incorrect password')
        return None
    return this_account_dict['balance']


def deposit(account_num: int, amount: int, password: str) -> int or None:
    global account_list
    this_account_dict = account_list[account_num]
    if amount < 0:
        print('You cannot deposit a negative number!')
        return None

    if password != this_account_dict['password']:
        print('Incorrect password')
        return None

    this_account_dict['balance'] += amount
    return this_account_dict['balance']


def withdraw(account_num: int, amount: int, password: str) -> int or None:
    global account_list
    this_account_dict = account_list[account_num]
    if amount > this_account_dict['balance']:
        print('You don`t have enough money in your account')
        return None

    elif amount < 0:
        print('You cannot withdraw a negative amount!')
        return None

    if password != this_account_dict['password']:
        print('Incorrect password')
        return None

    this_account_dict['balance'] -= amount
    return this_account_dict['balance']


new_account('Joe', 2000, 'qwerty')

new_account('Mary', 4000, 'soup')

while True:
    print()
    print('Press "b" to get the balance')
    print('Press "d" to make a deposit')
    print('Press "w" to make a withdrawal')
    print('Press "n" to create a new account')
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

    elif action == 'n':
        print('New Account:')
        user_name = input('What is your name? ')
        user_starting_amount = int(input('What is the amount of '
                                         'your initial deposit? '))
        user_password = input('What password would you like '
                              'to use for this account? ')
        user_account_number = len(account_list)
        new_account(user_name, user_starting_amount, user_password)
        print('Your new account number is:', user_account_number)

    elif action == 's':
        print('Show:')
        show(int(input('Please enter your account number: ')))

    elif action == 'q':
        break

    else:
        print('Sorry, you typed in an unknown command')

print('Done')
