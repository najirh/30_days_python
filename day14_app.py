
# Banking applications
class Account:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance

        
        # print(f"Current balance is {balance}")
            
    # medthod 1 debit method
    def debit(self, amount):
        self.balance -= amount
        print(f"Your account is being debited by {amount}")
        print(f"Your account balance is {self.balance}")
        
    # credit method
    def credit(self, amount):
        self.balance += amount
        print(f"Your account is being credited by {amount}")
        print(f"Your account balance is {self.balance}")
        
    def get_balance(self):
        print(f"Your account balance is {self.balance}")
    
# this object 
acc1 = Account(101, 15000)
acc2 = Account(102,5000)
acc3 = Account(103, 11000)

# transactions
print(acc1.get_balance())

# debit 10000
acc1.debit(10000)
acc1.credit(2000)


# check balance
print(acc2.balance)
# end







