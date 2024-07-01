# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

class Bank:
    
    def __init__(self):
        self.customers = {} # key: account_number; value: balance
    
    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.customers:
            self.customers[account_number] = initial_balance
            return 'Account is created successfully.'
        return 'Account already existed.'
    
    def make_deposit(self, account_number, deposit_amount):
        if account_number in self.customers:
            self.customers[account_number] += deposit_amount
            return f'{deposit_amount} is added to your account.'
        return 'Account is not found.'
    
    def make_withdrawal(self, account_number, withdraw_amount):
        if account_number in self.customers:
            if self.customers[account_number] < withdraw_amount:
                return f'You do not have enough money in your account.'
            self.customers[account_number] -= withdraw_amount
            return f'{withdraw_amount} is taken out from your account.'
        return 'Account is not found.'
        
    def show_balance(self, account_number):
        if account_number in self.customers:
            return f'Your balance is {self.customers[account_number]}.'
        return 'Account is not found.'
    