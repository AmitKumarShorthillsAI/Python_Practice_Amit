# Defining the outer class 'Bank'
class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name  # Instance variable

    # Method to display bank details
    def show_bank_name(self):
        print(f"Bank Name: {self.bank_name}")

    # Defining the inner class 'Account'
    class Account:
        def __init__(self, account_holder, balance):
            self.account_holder = account_holder  # Instance variable
            self.balance = balance  # Instance variable

        # Method to deposit money
        def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                print(f"Deposited ${amount}. New balance: ${self.balance}")
            else:
                print("Invalid deposit amount!")

        # Method to withdraw money
        def withdraw(self, amount):
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
            else:
                print("Invalid withdrawal amount or insufficient funds!")

        # Method to display account details
        def display_info(self):
            print(f"Account Holder: {self.account_holder}, Balance: ${self.balance}")

# Creating an instance of the outer class (Bank)
bank = Bank("Shorthills Bank")
bank.show_bank_name()  # Output: Bank Name: Shorthills Bank

# Creating an instance of the inner class (Account)
account = Bank.Account("Amit", 5000)

# Accessing inner class methods
account.display_info()   # Output: Account Holder: Amit, Balance: $5000
account.deposit(1500)    # Output: Deposited $1500. New balance: $6500
account.withdraw(2000)   # Output: Withdrew $2000. Remaining balance: $4500
