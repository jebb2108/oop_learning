# Тестовая программа, использующая счета
# Версия 1, использующая явные переменные для каждого объекта Account

from account import *

# Создаем два счета
o_joes_account =Account('Joe', 100, 'JoesPassword')
print("Created an account for Joe")
o_marys_account = Account('Mary', 12345, "MarysPassword")
print("Created an account for Mary")
o_joes_account.show()
o_marys_account.show()
print()

# Вызываем разные методы для для разных аккаунтов
print('Calling methods of the two accounts ...')
o_joes_account.deposit(50, 'JoesPassword')
o_marys_account.withdraw(345, 'MarysPassword')
o_marys_account.deposit(100, 'MarysPassword')

# Отображаем счета
o_joes_account.show()
o_marys_account.show()

# Создаем новый счет с информацией от пользователя
print()
user_name = input('What is the name for the new user account? ')
user_balance = input('What is the starting balance for this account? ')
user_password = input('What is the password you want to use for this '
                      'account? ')
o_new_account = Account(user_name, user_balance, user_password)

# отображаем вновь созданный счет пользователя
o_new_account.show()

o_new_account.deposit(100, user_password)
user_balance = o_new_account.get_balance(user_password)
print()
print('After depositing 100, the user`s balance is:', user_balance)

# Отображаем новый счет
o_new_account.show()