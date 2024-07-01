from classes import bank

# Create an instance of the Bank class
bank = bank.Bank()

# Create customer accounts and perform account operations
acno1= "SB-123"
damt1 = 1000
print("New a/c No.: ",acno1,"Deposit Amount:",damt1)
print(bank.create_account(acno1, damt1))

acno2= "SB-124"
damt2 = 1500
print("New a/c No.: ",acno2,"Deposit Amount:",damt2)
print(bank.create_account(acno2, damt2))

wamt1 = 600
print("\nDeposit Rs.",wamt1,"to A/c No.",acno1)
print(bank.make_deposit(acno1, wamt1))

wamt2 = 350
print("Withdraw Rs.",wamt2,"From A/c No.",acno2)
print(bank.make_withdrawal(acno2, wamt2))

print("A/c. No.",acno2)
print(bank.show_balance(acno2))

wamt3 = 1200
print("Withdraw Rs.",wamt3,"From A/c No.",acno2)
print(bank.make_withdrawal(acno2, wamt3))

acno3 = "SB-134"
print("A/c. No.",acno3)
print(bank.show_balance(acno3))  # Non-existent account number 

print(bank.customers)