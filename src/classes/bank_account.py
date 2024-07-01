# Write a  Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.

class BankAccount:
    def __init__(self, account_number, date_of_opening, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
        
    def deposit(self, amount):
        self.balance += amount
        print(f'You deposited {amount}.')

    
    def withdraw(self, amount):
        if self.balance < amount:
            print('You do not have enough money in your account.')
        else:
            self.balance -= amount
            print(f'You withdrawn {amount}.')
    
    def check_balance(self):
        print(f'Your balance is {self.balance}.')



# Input customer details
ac_no_1 = BankAccount(2345, "01-01-2011", 1000, "Toninho Takeo")
ac_no_2 = BankAccount(1234, "11-03-2011", 2000, "Astrid Rugile")
ac_no_3 = BankAccount(2312, "12-01-2009", 3000, "Orli Kerenza")
ac_no_4 = BankAccount(1395, "01-01-2011", 3000, "Luciana Chika")
ac_no_5 = BankAccount(6345, "01-05-2011", 4000, "Toninho Takeo")

print("=============================")

# Current balance is $3000.
# $1000 has been deposited in your account.
ac_no_4.deposit(1000)
ac_no_4.check_balance()
# Your current balance $4000.
# You want to withdraw $5000
ac_no_4.withdraw(5000)
# Output:
# Insufficient balance.
#The customer withdraw $3400.
ac_no_4.withdraw(3400)
ac_no_4.check_balance()