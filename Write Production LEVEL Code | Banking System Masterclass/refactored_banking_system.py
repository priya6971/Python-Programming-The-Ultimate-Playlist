from abc import ABC, abstractmethod

# --------------------------------
# Decorator 
# --------------------------------
def transaction_logger(func):
    def wrapper(self, amount):
        print(f'[LOG] {func.__name__.upper()} of {amount} initiated')
        result = func(self, amount)
        print(f'[LOG] Transaction completed successfully\n')
        return result
    return wrapper

# --------------------------------
# Abstract Class (Abstraction) 
# --------------------------------
class Account(ABC):
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder 
        self._balance = balance
    
    @staticmethod
    def validate_amount(amount):
        return amount > 0
    
    ## add the money to the account
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f'Deposited {amount}. New balance is {self._balance}')
        else:
            print('Deposited amount must be positive')
    
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display(self):
        pass

# ---------------------------------------
# LOAN APPLICATION [MULTIPLE INHERITANCE]
# ---------------------------------------
class LoanApplication:
    def apply_loan(self, amount):
        print(f'Loan of {amount} approved for {self.account_holder}')

# --------------------------------
# SAVINGS ACCOUNT [INHERITANCE] 
# --------------------------------       
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    
    @transaction_logger
    def withdraw(self, amount):
        if amount <= self._balance and amount > 0:
            self._balance -= amount
            print(f'{amount} withdrawn. New balance: {self._balance}')
        else:
            print('Insufficient funds')


    ## add_interest -> add the interest in the savings account
    def add_interest(self):
        interest = self._balance * self.interest_rate / 100
        self._balance += interest
        print(f'Interest added:{interest}. New balance: {self._balance}')

    ## display method to display the account details
    def display(self):
        print(f'Account Number: {self.account_number}, Balance: {self._balance}')
# --------------------------------
# CURRENT ACCOUNT [INHERITANCE] 
# --------------------------------  
class CurrentAccount(Account):
    ## __init__() => to initialize the attributes entered by the user
    ## constructor
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    

   ## Polymorphism: withdraw the money from the account
    @transaction_logger
    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft_limit and amount > 0:
            self._balance -= amount
            print(f'{amount} withdrawn. New balance: {self._balance}')
        else:
            print('Overdraft limit exceeded') 

    ## Polymorphism: display the account details with the overdraft limit
    def display(self):
        print(f'Current Account Number: {self.account_number}, Balance: {self._balance}, Overdraft limit: {self.overdraft_limit}')

# --------------------------------
# MULTIPLE INHERITANCE 
# -------------------------------- 
class PremiumAccount(SavingsAccount, LoanApplication):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance, interest_rate)
    
    def display(self):
        print(f'[Premium] Acc: {self.account_number}, Balance: {self._balance}, Perks Enabled.')

print('\n---SAVINGS ACCOUNT---')
sa = SavingsAccount('SA101', 'Priya Bhatia', 50000, 5)
sa.deposit(10000)
sa.withdraw(5000)
sa.add_interest()
sa.display()

ca = CurrentAccount('CA101', 'Radha Rani', 500000, 100000)
ca.withdraw(550000)
ca.display()

pa = PremiumAccount('PA301', 'Sushma', 1000000, 0)
pa.apply_loan(100000)
pa.display()