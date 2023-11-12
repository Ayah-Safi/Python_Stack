class User :
    def __init__(self,name,balance= 0) :
        self.name = name
        self.balance = balance
    
    def make_deposit(self,value):
        self.balance += value
        return self
        
    def make_withdrawal(self,value):
        self.balance -= value
        return self
        
    def display_user_balance(self):
        print(self.name, self.balance)
        return self
        
    def transfer_money(self,other_user,amount):
        self.balance -= amount
        other_user.balance +=amount
        return self


user1 = User("mutaz",5000)
user2 = User("khaled",2000)
user3 = User("ayah",3000)


user1.make_deposit(200).make_deposit(500).make_deposit(700).make_withdrawal(100).display_user_balance()
user2.make_deposit(100).make_deposit(300).make_withdrawal(100).make_withdrawal(200).display_user_balance()
user3.make_deposit(100).make_withdrawal(300).make_withdrawal(100).make_withdrawal(200).display_user_balance()



