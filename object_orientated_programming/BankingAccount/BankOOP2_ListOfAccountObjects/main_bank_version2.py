""" Тестовая программа, использующая счета """
""" Версия 2, с использованием списка счетов """

# берем весь код из файла  класса Account
from account import Account

# Начинаем с пустого списка счетов
account_list = []

# Создаем два счета
o_account = Account('Joe', 100, 'JoesPassword')
account_list.append(o_account)
print('Joes account number is 0')

o_account = Account('Mary', 12345, 'MarysPassword')
account_list.append(o_account)
print('Marys account number is 1')

account_list[0].show()
account_list[1].show()
print()

# Вызываем разные методы для разных счетов
print('Calling methods of the two accounts')
account_list[0].deposit(50, 'JoesPassword')
account_list[1].withdraw(345, 'MarysPassword')
account_list[1].deposit(100, 'MarysPassword')

# Отображаем счета
account_list[0].show()
account_list[1].show()

# Создаем новый счет с информацией от пользователя
print()
user_name = input('What is the name for the new user account? ')
user_balance = int(input('What is the starting balance for this account? '))
user_password = input('What is the password you want to use for this '
                      'account? ')
o_account = Account(user_name, user_balance, user_password)
account_list.append(o_account)  # Добавляем к списку счетов

# Отображаем вновь созданный счет пользователя
print('Created new account, account number is 2')
account_list[2].show()

# Вносим 100 на новый счет
account_list[2].deposit(100, user_password)
user_balance = account_list[2].get_balance(user_password)
print()
print('After depositing 100, the users balance is:', user_balance)

# Отображаем новый счет
account_list[2].show()
print()
print(account_list)