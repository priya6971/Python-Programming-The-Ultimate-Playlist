class Account: 
    ## __init__() => to initialize the attributes entered by the user
    ## constructor
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance # private attribute
    

    ## add the money to the account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposited {amount}. New balance is {self.__balance}')
        else:
            print('Deposited amount must be positive')
    
    ## withdraw the money from the account
    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
            print(f'{amount} withdrawn. New balance: {self.__balance}')
        else:
            print('Insufficient funds')

    ## display method to display the account details
    def display(self):
        print(f'Account Number: {self.account_number}, Balance: {self.__balance}')



acc1 = Account('AC123', 'Priya Bhatia', 10000)
acc1.display()