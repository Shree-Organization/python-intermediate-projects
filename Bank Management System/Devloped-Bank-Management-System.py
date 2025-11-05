class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ₹{amount}. \nNew balance: ₹{self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ₹{amount}. \nNew balance: ₹{self.balance}.")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number not in self.accounts:
            new_account = Account(account_number, account_holder)
            self.accounts[account_number] = new_account
            print(f"Account created for {account_holder}.")
        else:
            print("Account already exists.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number].get_balance()
            print(f"Balance for account {account_number}: ${balance}.")
        else:
            print("Account not found.")

    def display_accounts(self):
        if self.accounts:
            print("Accounts in the bank:")
            for account in self.accounts.values():
                print(account)
        else:
            print("No accounts in the bank.")


def main():
    bank = Bank()

    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Display All Accounts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            bank.create_account(account_number, account_holder)
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(account_number, amount)
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(account_number, amount)
        elif choice == '4':
            account_number = input("Enter account number: ")
            bank.check_balance(account_number)
        elif choice == '5':
            bank.display_accounts()
        elif choice == '6':
            print("🙏 Thank you for visiting 🙏 \nExiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

