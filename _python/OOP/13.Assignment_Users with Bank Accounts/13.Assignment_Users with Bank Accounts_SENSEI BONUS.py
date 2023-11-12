class User:
    def __init__(self, name):
        self.name = name
        self.accounts = {}  

    def create_account(self, account_id, balance=0, interest_rate=0.01):
        self.accounts[account_id] = BankAccount(balance, interest_rate)
        return self

    def make_deposit(self, account_id, value):
        self.accounts[account_id].deposit(value)
        return self

    def make_withdrawal(self, account_id, value):
        self.accounts[account_id].withdraw(value)
        return self

    def display_user_balance(self, account_id):
        print(f"{self.name}'s Balance for Account {account_id}: ${self.accounts[account_id].balance}")
        return self


class BankAccount:
    def __init__(self,balance = 0,interest_rate = 0.01):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.interest_rate
        else:
            print("Insufficient Current Balance, Yield Interest is not Applicable")
        return self