""" Интерактивная тестовая программа создания нового словаря счетов """
""" Версия 4 с интерактивным меню """
from account import Account

accounts_dict = {}
next_account_number = 0

# Создаем два счета
o_account = Account('Joe', 100, 'JoesPassword')
joes_account_number = next_account_number
accounts_dict[joes_account_number] = o_account
print('Joes account number is:', joes_account_number)
next_account_number += 1

o_account = Account('Mary', 12345, 'MarysPassword')
marys_account_number = next_account_number
accounts_dict[marys_account_number] = o_account
print('Marys account number is:', marys_account_number)
next_account_number += 1

while True:
    print()
    print('Press "b" to get the balance')
    print('Press "d" to make a deposit')
    print('Press "o" to open a new account')
    print('Press "w" to make a withdrawal')
    print('Press "s" to show all accounts')
    print('Press "q" to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]

    if action == 'b':
        print('*** Get Balance ***')
        user_account_number = int(input('Please enter your '
                                        'account number: '))
        user_account_password = input('Enter the password: ')
        o_account = accounts_dict[user_account_number]
        the_balance = o_account.get_balance(user_account_password)
        if the_balance is not None:
            print("Your balance is:", the_balance)

    elif action == 'd':
        print('*** Deposit ***')
        user_account_number = int(input('Please enter your '
                                        'account number: '))
        user_account_password = input('Enter the password: ')
        user_amount_to_deposit = int(input('Enter amount to deposit: '))
        o_account = accounts_dict[user_account_number]
        the_balance = o_account.deposit(user_amount_to_deposit, user_account_password)
        if the_balance is not None:
            print('Your new balance is:', the_balance)

    elif action == 'o':
        print('*** Open Account ***')
        account_username = input('What is the name for the new account: ')
        account_balance = int(input('What is the starting balance for this account: '))
        account_password = input('What is the password you want to use for your account: ')
        o_account = Account(account_username, account_balance, account_password)
        accounts_dict[next_account_number] = o_account
        print('Your new account number is', next_account_number)
        next_account_number += 1
        print()

    elif action == 's':
        print('Show:')
        for user_account_number in accounts_dict:
            o_account = accounts_dict[user_account_number]
            print(' Account number:', user_account_number)
            o_account.show()

    elif action == 'q':
        break

    elif action == 'w':
        print('*** Withdrawal ***')
        user_account_number = int(input('Please enter your '
                                        'account number: '))
        user_account_password = input('Enter the password: ')
        user_withdrawal_amount = int(input('Enter amount to withdraw: '))
        o_account = accounts_dict[user_account_number]
        the_balance = o_account.withdraw(user_withdrawal_amount, user_account_password)
        if the_balance is not None:
            print('Withdrew:', user_withdrawal_amount)
            print('Your new balance is:', the_balance)

    else:
        print('Sorry, that was not a valid action. Please try again.')

print('Done')
