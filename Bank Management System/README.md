# 🏦 Bank Management System

A Python-based banking application built using Object-Oriented Programming (OOP).

This project provides two banking models:

Simple Bank Class – Demonstrates the basics of deposits, withdrawals, and balance handling.

Full Bank Management System – A complete menu-driven system with multiple accounts support.

## ✨ Features

🔹 Create Accounts – Open new bank accounts with holder name & account number.

🔹 Deposit / Withdraw Money – Update account balance securely.

🔹 Balance Inquiry – Check available balance.

🔹 Multiple Accounts – Manage multiple users at once.

🔹 View All Accounts – List every account with details.

🔹 Validation – Prevents overdrawing and duplicate account numbers.

🔹 Bank Greeting – Welcomes users to the bank.

## 🛠️ Technologies

Language: Python 3.x

Concepts:

  Classes & Objects

  Encapsulation

  Static Methods

  Menu-driven CLI interaction

## ⚡ Quick Start
1️⃣ Clone the Repository
```
git clone https://github.com/your-username/bank-management.git
cd bank-management
```

2️⃣ Run the Program
```
python bank_management.py
```

🧑‍💻 Example (Simple Bank Class)
```python
acc1 = bank("Mantra Patil", 214975324355, 1000)

print("Account holder:", acc1.name) 
print("Account number:", acc1.account_no)
print("Initial Balance:", acc1.balance)
print("After Deposit:", acc1.deposit(500))
print("After Withdrawal:", acc1.withdraw(300))
print("Attempt to Withdraw More Than Balance:", acc1.withdraw(1500))
print("Bank name:", acc1.bank_name)
```

✅ Sample Output:
```
Account holder: Mantra Patil
Account number: 214975324355
Initial Balance: 1000
After Deposit: 1500
After Withdrawal: 1200
Attempt to Withdraw More Than Balance: Insufficient funds
Bank name: SBI Bank
```

🧑‍💻 Example (Menu-driven Bank System)
```
Bank Management System
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Display All Accounts
6. Exit

```
✅ Workflow Example:
```
Enter your choice: 1
Enter account number: 1001
Enter account holder name: Alice
Account created for Alice.

Enter your choice: 2
Enter account number: 1001
Enter amount to deposit: 2000
Deposited: ₹2000. 
New balance: ₹2000.

Enter your choice: 3
Enter account number: 1001
Enter amount to withdraw: 500
Withdrew: ₹500. 
New balance: ₹1500.
```

📂 Project Structure
```
bank-management/
│── bank_management.py   # Main program
│── README.md            # Documentation
```

##  🚀 Future Improvements

🔹 Track total number of accounts created with a counter.

🔹 Add interest calculation & loan features.

🔹 Export/import account data to CSV/JSON for persistence.

🔹 Build a GUI app using Tkinter or a Web App using Flask/Django.

🔹 Add PIN/Password authentication for security.

👨‍💻 Author

Crafted with 💡 & 💻 by Mantra Patil

*👉 Pro Tip: This project is great for learning Python OOP and can be extended into a real-world digital banking simulator.*
