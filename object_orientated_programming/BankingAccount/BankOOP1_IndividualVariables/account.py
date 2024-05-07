""" Класс счета """

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amount_to_deposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        if amount_to_deposit < 0:
            print('You cannot deposit a negative amount')
            return None

        self.balance += amount_to_deposit
        return self.balance

    def withdraw(self, amount_to_withdraw, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        if amount_to_withdraw > self.balance:
            print('Sorry, you don`t have enough money in '
                  'your account')
            return None

        self.balance -= amount_to_withdraw
        return self.balance

    def get_balance(self, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None

        return self.balance

    # Добавлено для отладки
    def show(self):
        print('Show:')
        print('       Name:', self.name)
        print('       Balance:', self.balance)
        print('       Password:', self.password)
        print()