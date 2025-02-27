class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Encapsulated (private) attribute

    # Public method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money from the account
    def withdraw(self, amount):
        if self.__check_sufficient_funds(amount):
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds.")

    # Public method to get the current balance (getter)
    def get_balance(self):
        return self.__balance

    # Private method to check if the account has sufficient funds for a withdrawal
    def __check_sufficient_funds(self, amount):
        return self.__balance >= amount

    # Private method to calculate the interest (just an example)
    def __calculate_interest(self):
        return self.__balance * 0.05

# Creating an instance of BankAccount
account = BankAccount("John", 1000)

# Public methods (interactions)
account.deposit(500)  # Works fine
account.withdraw(300)  # Works fine
print(account.get_balance())  # Works fine: 1200