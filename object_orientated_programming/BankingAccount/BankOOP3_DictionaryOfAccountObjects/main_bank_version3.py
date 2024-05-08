""" Тестовая программа, использующая счета """
""" Версия 3 с использованием словаря счетов """

# Берем весь код из файла класса Account
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

accounts_dict[joes_account_number].show()
accounts_dict[marys_account_number].show()
print()

# Вызываем разные методы для разных счетов
print('Calling methods of the two accounts')
accounts_dict[joes_account_number].deposit(50, 'JoesPassword')
accounts_dict[marys_account_number].withdraw(345, 'MarysPassword')
accounts_dict[marys_account_number].deposit(100, 'MarysPassword')

# Отображаем счета
accounts_dict[joes_account_number].show()
accounts_dict[marys_account_number].show()

# Создаем новый счет с информацией от пользователя
print()
user_name = input('What is the name for the new user account? ')
user_balance = int(input('What is the starting balance for this account? '))
user_password = input('What is the password you want to use for this '
                      'account? ')
o_account = Account(user_name, user_balance, user_password)
user_account_number = next_account_number
accounts_dict[next_account_number] = o_account  # Добавляем к списку счетов
next_account_number += 1

# Отображаем вновь созданный счет пользователя
print('Created new account, account number is 2')
accounts_dict[user_account_number].show()

# Вносим 100 на новый счет
accounts_dict[user_account_number].deposit(100, user_password)
user_balance = accounts_dict[user_account_number].get_balance(user_password)
print()
print('After depositing 100, the users balance is:', user_balance)

# Отображаем новый счет
accounts_dict[user_account_number].show()
print()
print(accounts_dict)
