# If you've been following along, 
# you're going to utilize the User 
# class we've been discussing for 
# this assignment.

# For this assignment, we'll add 
# some functionality to the User class:

# -make_withdrawal(self, amount)          #have this method decrease the user's balance by the amount specified
# -display_user_balance(self)          #have this method print the user's name and account balance to the terminal
#     eg. "User: Guido van Rossum, Balance: $150
    
# **BONUS:
# transfer_money(self, other_user, amount)            #have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User Name: {self.name}\nAccount Balance: ${self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


jim = User("Jim")
jim.make_deposit(133)
jim.make_deposit(133)
jim.make_deposit(134)
jim.make_withdrawal(13)
jim.display_user_balance()

jake = User("Jake")
jake.make_deposit(50)
jake.make_deposit(51)
jake.make_withdrawal(1)
jake.make_withdrawal(1)
jake.display_user_balance()

john = User("John")
john.make_deposit(72)
john.make_withdrawal(3)
john.make_withdrawal(6)
john.make_withdrawal(9)
john.display_user_balance()

jim.transfer_money(john, 18)
jim.display_user_balance()
jake.display_user_balance()