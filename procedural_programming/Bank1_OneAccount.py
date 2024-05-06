"""

Без ООП
Банк версия 1
Единственный счет

"""

account_name = 'Joe'
account_balance = 100
account_password = 'soup'

while True:
    print()
    print('Press "b" to get the balance')
    print('Press "d" to make a deposit')
    print('Press "w" to make a withdrawal')
    print('Press "s" to show the account')
    print('Press "q" to quit')

    action = input('What do you want to do? ')
    action = action.lower() # Переводит в нижний регистр
    action = action[0] # Использует первую букву
    print()

    if action == 'b':
        print('Get Balance:')
        user_password = input('Please enter the password: ')
        if user_password != account_password:
            print('Incorrect password')
        else:
            print('Your balance is:', account_balance)

    elif action == 'd':
        print('Deposit:')
        user_deposit_amount = input('Please enter amount to deposit: ')
        user_deposit_amount = int(user_deposit_amount)
        user_password = input('Please enter the password: ')
        if user_deposit_amount < 0:
            print('You cannot deposit a negative amount!')
        elif user_password != account_password:
            print('Incorrect password')
        else: # OK
            account_balance += user_deposit_amount

    elif action == 's':
        print('Show:')
        print('       Name:', account_name)
        print('       Balance:', account_balance)
        print('       Password:', account_password)
        print()

    elif action == 'q':
        break

    elif action =='w':
        print('Withdrawal:')
        user_withdrawal_amount = input('Please enter the amount to '
                                       'withdraw: ')
        user_withdrawal_amount = int(user_withdrawal_amount)
        user_password = input('Please enter the password: ')

        if user_withdrawal_amount < 0:
            print('You cannot withdraw a negative amount!')

        elif user_password != account_password:
            print('Incorrect password')

        elif user_withdrawal_amount > account_balance:
            print('You cannot withdraw more than you have in your '
                  'account')
        else:
            account_balance -= user_withdrawal_amount
            print('Your new balance is:', account_balance)


print('Done')