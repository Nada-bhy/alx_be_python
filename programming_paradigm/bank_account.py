class BankAccount:
    def __init__(self, initial_balance=0):
        self.accoount_balance = initial_balance
        
    def deposit (self, amount):
        self.accoount_balance += amount
        
    def withdraw(self, amount):
        if amount <= self.accoount_balance:
            self.accoount_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.accoount_balance}")