from Account import BankAccount

account1 = BankAccount( 5, 100)

account2 = BankAccount( 5, 1000)


account1.deposit(200).deposit(100).deposit(300).yield_interest().display_account_info()

account2.deposit(3000).deposit(200).withdraw(500).withdraw(1000).withdraw(2500).withdraw(500).display_account_info()


BankAccount.printAllAccountsInfo()