""" Основная программа, контролирующая банк, состоящая из счетов """

# Берем весь код из класса банка
from bank import Bank

# Создаем экземпляр банка
o_bank = Bank()

# Основной код
# создаем два тестовых счета
joes_account_number = o_bank.create_account('Joe', 100, 'JoesPassword')
print('Joes`s account number is:', joes_account_number)

marys_account_number = o_bank.create_account('Mary', 12345, 'MarysPassword')
print('Mary`s account number is:', marys_account_number)

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

    if action == 'b':
        o_bank.balance()

    elif action == 'c':
        o_bank.close_account()

    elif action == 'd':
        o_bank.deposit()

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

print('Done')
