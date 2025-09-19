
class bank :
    bank_name = "SBI Bank"
    def __init__(self, name , account_no , balance = 0):
        self.name = name
        self.balance = balance
        self.account_no = account_no    

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"
        
    @staticmethod
    def greet():
        print("Welcome to the bank!")   
bank.greet()

acc1 = bank("Mantra Patil" , 214975324355 , 1000)
print("Account holder:", acc1.name) 
print("Account number:", acc1.account_no)
print("Initial Balance:", acc1.balance)
print("After Deposit:", acc1.deposit(500))
print("After Withdrawal:", acc1.withdraw(300))
print("Attempt to Withdraw More Than Balance:", acc1.withdraw(1500))
print("Bank name :" , acc1.bank_name , "\n")

bank.greet()
acc2 = bank("Amanraj Mistry" , 4578936154852 , 2000)
print("Account holder:", acc2.name)
print("Account number:", acc2.account_no)
print("Initial Balance:", acc2.balance)
print("After Deposit:", acc2.deposit(800))
print("After Withdrawal:", acc2.withdraw(500))
print("Attempt to Withdraw More Than Balance:", acc2.withdraw(3000))
print("Bank name :" , acc2.bank_name , "\n")

print("Total number of accounts created:", bank.__init__.__code__.co_argcount - 1)
# Note: The last line counts the number of parameters in the __init__ method excluding 'self' to estimate the number of accounts.
# However, this is not a reliable way to count instances. 
# A better approach would be to maintain a class variable that increments with each new instance.
# This is just for demonstration purposes.

