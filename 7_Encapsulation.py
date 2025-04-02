# Encapsulation is a fundamental concept in OOP that restricts direct access to an object's data.
# It helps to protect the integrity of the data and hide the internal representation of the object.
class BankAccount:
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder  # Public attribute
        self._balance = balance  # Protected attribute (single underscore)
        self.__pin = pin  # Private attribute (double underscore)
    
    # Public method to display account info
    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self._balance}")
    
    # Protected method (used internally)
    def _update_balance(self, amount):
        self._balance += amount
        print(f"Balance updated. New Balance: ${self._balance}")
    
    # Private method (used internally for security)
    def __validate_pin(self, entered_pin):
        return self.__pin == entered_pin
    
    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._update_balance(amount)
        else:
            print("Deposit amount must be positive!")
    
    # Public method to withdraw money
    def withdraw(self, amount, entered_pin):
        if self.__validate_pin(entered_pin):
            if 0 < amount <= self._balance:
                self._update_balance(-amount)
                print(f"Withdrawal successful. Amount withdrawn: ${amount}")
            else:
                print("Invalid withdrawal amount or insufficient funds!")
        else:
            print("Incorrect PIN! Access denied.")
    
# Execution
if __name__ == "__main__":
    account = BankAccount("John Doe", 1000, 1234)
    
    print("\nAccount Information:")
    account.display_account_info()
    
    print("\nDepositing Money:")
    account.deposit(500)
    
    print("\nWithdrawing Money:")
    account.withdraw(300, 1234)  # Correct PIN
    account.withdraw(200, 9999)  # Incorrect PIN
    
    # Accessing public attribute
    print("\nAccessing Public Attribute:")
    print("Account Holder:", account.account_holder)
    
    # Accessing protected attribute (not recommended but possible)
    print("\nAccessing Protected Attribute:")
    print("Balance:", account._balance)  # Not recommended
    
    # Trying to access private attribute (will fail)
    print("\nTrying to Access Private Attribute:")
    try:
        print(account.__pin)  # This will raise an AttributeError
    except AttributeError:
        print("Cannot access private attribute __pin!")