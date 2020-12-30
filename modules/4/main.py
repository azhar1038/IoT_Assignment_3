from account import Account

acc = Account(int(input("Enter initial account balance: ")))
deposit_amount = int(input("Enter amount to deposit: "))
acc.deposit(deposit_amount)
print("Current Balance: ", acc.check_balance())
withdraw_amount = int(input("Enter amount to withdraw: "))
acc.withdraw(withdraw_amount)
print("Current Balance: ", acc.check_balance())
acc.set_minimum(3000)
print("Minimum balance has been changed to 3000")
withdraw_amount = int(input("Enter amount to withdraw: "))
acc.withdraw(withdraw_amount)
print("Current Balance: ", acc.check_balance(), "--- Minimum required: ", acc.get_minimum())
