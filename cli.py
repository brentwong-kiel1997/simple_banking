import sys
from banking_system import Bank

def exit_system():
    """Cleanly exit the application."""
    print("Goodbye!")
    sys.exit(0)

def main():
    bank = Bank()

    MENU = """
Simple Banking System
1. Create Account
2. Deposit
3. Withdraw
4. Transfer
5. Check Balance
6. Exit
(Type 'exit' or 'quit' anytime to leave)
> """

    while True:
        choice = input(MENU).strip().lower()

        # Allow textual exit commands
        if choice in {"6", "exit", "quit"}:
            exit_system()

        try:
            if choice == "1":
                name = input("Owner Name: ").strip()
                bal = float(input("Starting Balance: ").strip())
                acc_id = bank.create_account(name, bal)
                print(f"Account created: ID {acc_id}")

            elif choice == "2":
                acc = input("Account ID: ").strip()
                amt = float(input("Deposit Amount: ").strip())
                bank.deposit(acc, amt)
                print("Deposit successful.")

            elif choice == "3":
                acc = input("Account ID: ").strip()
                amt = float(input("Withdraw Amount: ").strip())
                bank.withdraw(acc, amt)
                print("Withdrawal successful.")

            elif choice == "4":
                a = input("From Account ID: ").strip()
                b = input("To Account ID: ").strip()
                amt = float(input("Transfer Amount: ").strip())
                bank.transfer(a, b, amt)
                print("Transfer successful.")

            elif choice == "5":
                acc = input("Account ID: ").strip()
                bal = bank.check_balance(acc)
                print(f"Current balance: {bal}")

            else:
                print("Invalid option. Please choose 1–6, or type 'exit' to quit.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
