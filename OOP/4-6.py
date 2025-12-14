from bank_account import BankAccount

def main():
    account = BankAccount("12345655559090111100007722")

    account.display_balance()
    account.deposit(25.30)
    account.display_balance()
    account.withdraw(31.70)
    account.display_balance()
    account.withdraw(14.00)
    account.display_balance()

if __name__ == "__main__":
    main()
