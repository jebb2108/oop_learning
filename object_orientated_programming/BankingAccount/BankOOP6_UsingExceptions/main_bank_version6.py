""" Основная программа, контролирующая банк, состоящий из счетов """
from bank import *

# Создаем экземпляр банка
o_bank = Bank('9 to 5', '123 Main Street, Moscow, Russia', '+7(911) 123-45-67')

# Основной код
while True:
    print()
    print('To get an account balance, press "b"')
    print('To close an account an account, press "c"')
    print('To make a deposit, press "d"')
    print('To open a new account, press "o"')
    print('To show all accounts, press "s" ')
    print('To make a withdrawal, press "w" ')
    print('Press "q" to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    try:
        if action == 'b':
            o_bank.balance()
        elif action == 'c':
            o_bank.close_account()
        elif action == 'd':
            o_bank.deposit()
        elif action =='i':
            o_bank.get_info()
        elif action == 'o':
            o_bank.open_account()
        elif action == 's':
            o_bank.show()
        elif action == 'w':
            o_bank.withdraw()
        elif action == 'q':
            break

        else:
            print('Sorry, that was  not a valid action. Please try again.')

    except AbortTransaction as error:
        # выводим текст сообщения
        print(error)

print('Done')
