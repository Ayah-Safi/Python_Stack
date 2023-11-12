class User :
    def __init__(self,name,balance= 0) :
        self.name = name
        self.balance = balance
    
    def make_deposit(self,value):
        self.balance += value
        
    def make_withdrawal(self,value):
        self.balance -= value
        
    def display_user_balance(self):
        print(self.name, self.balance)
        
    def transfer_money(self,other_user,amount):
        self.balance -= amount
        other_user.balance +=amount


user1 = User("mutaz",5000)
user2 = User("khaled",2000)
user3 = User("ayah",3000)


user1.make_deposit(200)
user1.make_deposit(500)
user1.make_deposit(700)
user1.make_withdrawal(100)
user1.display_user_balance()

user2.make_deposit(100)
user2.make_deposit(300)
user2.make_withdrawal(100)
user2.make_withdrawal(200)
user2.display_user_balance()

user3.make_deposit(100)
user3.make_withdrawal(300)
user3.make_withdrawal(100)
user3.make_withdrawal(200)
user3.display_user_balance()

user1.transfer_money(user3,amount=100)
user1.display_user_balance()
user3.display_user_balance()
