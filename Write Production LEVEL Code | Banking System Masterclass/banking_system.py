class Account: 
    ## __init__() => to initialize the attributes entered by the user
    ## constructor
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    

    ## add the money to the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposited {amount}. New balance is {self.balance}')
        else:
            print('Deposited amount must be positive')
    
    ## withdraw the money from the account
    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(f'{amount} withdrawn. New balance: {self.balance}')
        else:
            print('Insufficient funds')

    ## display method to display the account details
    def display(self):
        print(f'Account Number: {self.account_number}, Balance: {self.balance}')

## Inheritance: SavingsAccount class inherited from the Account class
class SavingsAccount(Account):
    ## __init__() => to initialize the attributes entered by the user
    ## constructor
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    ## add_interest -> add the interest in the savings account
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f'Interest added:{interest}. New balance: {self.balance}')

    ## Polymorphism: display the account details with the interest rate
    def display(self):
        print(f'Savings Account Number: {self.account_number}, Balance: {self.balance}, Interest Rate: {self.interest_rate}')

## Inheritance: CurrentAccount class inherits from the Account class
class CurrentAccount(Account):
    ## __init__() => to initialize the attributes entered by the user
    ## constructor
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    

   ## Polymorphism: withdraw the money from the account
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit and amount > 0:
            self.balance -= amount
            print(f'{amount} withdrawn. New balance: {self.balance}')
        else:
            print('Overdraft limit exceeded') 

    ## Polymorphism: display the account details with the overdraft limit
    def display(self):
        print(f'Current Account Number: {self.account_number}, Balance: {self.balance}, Overdraft limit: {self.overdraft_limit}')


## objects creation
acc1 = Account('AC123', 'Priya Bhatia', 100000)
acc2 = Account('AC145', 'Lalit Kumar', 10000)
sa1 = SavingsAccount('SA123', 'Riya Sharma', 300000, 2)


print(acc1.display())
'''
print(acc2.balance)
acc2.deposit(20000)
acc2.withdraw(15000)
acc2.display()


print(sa1.balance)
sa1.withdraw(15000)
sa1.deposit(20000)
sa1.display()
'''

ca1 = CurrentAccount('CA123', 'Priya Bhatia', 1000000, 200000)
ca1.withdraw(1100000)
ca1.display()