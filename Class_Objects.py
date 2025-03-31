# Defining a class named 'BankAccount' which acts as blue print for creating bank account objects
class BankAccount:
    # Constructor (__init__) to initialize account attributes
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # Instance attribute (account owner name)
        self.balance = balance  # Instance attribute (default balance is 0)

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive!")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount!")

    # Method to display account details
    def display_info(self):
        print(f"Account Holder: {self.account_holder}, Balance: ${self.balance}")

# Creating an object (instance) of the BankAccount class
my_account = BankAccount("Amit", 1000)

# _____________________________Accessing methods directly_________________________________
# Accessing attributes and calling methods
my_account.display_info()  # Output: Account Holder: Amit, Balance: $1000

# Depositing money
my_account.deposit(500)  # Output: Deposited $500. New balance: $1500

# Withdrawing money
my_account.withdraw(200)  # Output: Withdrew $200. Remaining balance: $1300

# ______________________________Accessing attributes directly_______________________________
print(my_account.account_holder)  # Output: Amit
print(my_account.balance)  # Output: 1000

# ______________________________Accessing methods using class name___________________________
# Accessing methods using class name
BankAccount.withdraw(my_account, 100)  # Output: Withdrew $100. Remaining balance: $1200
# Accessing methods using class name
BankAccount.deposit(my_account, 300)  # Output: Deposited $300. New balance: $1500
# Accessing methods using class name
BankAccount.display_info(my_account)  # Output: Account Holder: Amit, Balance: $1500



# Listing all attributes and methods of the object
# print(dir(my_account))  # Shows available methods & attributes




# Deleting the object
# del my_account
# print(my_account.balance)  # This will raise NameError: name 'my_account' is not defined
