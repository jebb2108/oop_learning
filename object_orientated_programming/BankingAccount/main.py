from account import Account

o_account = Account('Joe Schmoe', 1000, 'magic')

new_balance = o_account.deposit(500, 'magic')
print(new_balance)

new_balance = o_account.withdraw(250, 'magic')
print(new_balance)

current_balance = o_account.get_balance('magic')
print(current_balance)