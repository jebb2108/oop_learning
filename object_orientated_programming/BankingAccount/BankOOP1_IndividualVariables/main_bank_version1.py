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