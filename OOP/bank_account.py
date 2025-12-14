class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: PLN {amount:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: PLN {amount:.2f}")
        else:
            print("Insufficient funds on the account")

    def display_balance(self):
        print(f"Bank Account No: {' '.join(self.account_number[i:i+4] for i in range(0, len(self.account_number), 4))}")
        print(f"Balance: PLN {self.balance:,.2f}")
