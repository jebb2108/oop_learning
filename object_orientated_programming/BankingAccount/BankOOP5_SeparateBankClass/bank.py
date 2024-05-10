""" Банк, управляющий словарем объектов Account """

from account import Account


class Bank():

    def __init__(self):
        self.accounts_dict = {}
        self.next_account_number = 0

    def create_account(self, the_name: str, the_starting_balance: int, the_password: str) -> int | object:
        o_account = Account(the_name, the_starting_balance, the_password)
        new_account_number = self.next_account_number
        self.accounts_dict[new_account_number] = o_account
        # Увеличивает на одну единицу для подготовки
        # следующей учетной записи
        self.next_account_number += 1
        return new_account_number

    def open_account(self):
        print('*** Open Account ***')
        user_name = input('What is the name for the new account? ')
        user_starting_amount = int(input('What is the starting balance '
                                         'for this account? '))
        user_password = input('What is the password you want to use for this account? ')

        user_account_number = self.create_account(user_name, user_starting_amount, user_password)
        print('Your new account number is:', user_account_number)
        print()

    def close_account(self):
        print('*** Close Account ***')
        user_account_number = int(input('What is your account number? '))
        user_password = input('What is your password? ')
        o_account = self.accounts_dict[user_account_number]
        the_balance = o_account.get_balance(user_password)
        if the_balance is not None:
            print('You had', the_balance, 'in your account, '
                                          'which is being returned to you.')
            # Удаляем учетную запись пользователя из словаря учетных записей
            del self.accounts_dict[user_account_number]
            print('Your account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        user_account_number = int(input('Please enter your account number: '))
        user_password = input('PLease enter the password: ')
        o_account = self.accounts_dict[user_account_number]
        the_balance = o_account.get_balance(user_password)
        if the_balance is not None:
            print('Your balance is:', the_balance)

    def deposit(self):
        print('*** Deposit ***')
        user_account_number = int(input('Please enter the account number: '))
        user_deposit_amount = int(input('Please enter amount to deposit: '))
        user_account_password = input('Enter the password: ')
        o_account = self.accounts_dict[user_account_number]
        the_balance = o_account.deposit(user_deposit_amount, user_account_password)
        if the_balance is not None:
            print('Your new balance is:', the_balance)

    def show(self):
        print('*** Show ***')
        for account_number in self.accounts_dict:
            o_object = self.accounts_dict[account_number]
            o_object.show()

    def withdraw(self):
        user_account_number = int(input('Please enter the account number: '))
        user_withdrawal_amount = int(input('Please enter amount to deposit: '))
        user_account_password = input('Enter the password: ')
        o_account = self.accounts_dict[user_account_number]
        the_balance = o_account.withdraw(user_withdrawal_amount, user_account_password)
        if the_balance is not None:
            print('Withdrew:', user_withdrawal_amount)
            print('Your new balance is:', the_balance)
