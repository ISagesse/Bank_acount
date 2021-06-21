from bank_acount import *

bond = BankAcount(15, 0)
israel = BankAcount(1, 0)

#The first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line 
#of code (i.e. chaining)
bond.deposit(150000).deposit(300000).deposit(1500000).withdraw(450000).yield_interest().display_account_info()

#The second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code
#(i.e. chaining)
israel.deposit(750).deposit(250).withdraw(50).withdraw(400).withdraw(20).withdraw(50).yield_interest().display_account_info()