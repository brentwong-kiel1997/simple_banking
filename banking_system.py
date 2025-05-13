import csv
import os

class Account:
    def __init__(self, account_id: str, owner_name: str, balance: float = 0.0):
        self.account_id = account_id
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Withdraw amount must be non-negative.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def __repr__(self):
        return f"Account({self.account_id!r}, {self.owner_name!r}, {self.balance!r})"


class Bank:
    def __init__(self, csv_path: str = "bank_state.csv"):
        self._csv_path = csv_path
        self._accounts: dict[str, Account] = {}
        self._next_id = 1

        # Load existing state if present
        if os.path.exists(self._csv_path):
            self.load_from_csv(self._csv_path)

    def _persist(self):
        """Save current state to CSV."""
        with open(self._csv_path, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["account_id", "owner_name", "balance"])
            for acct in self._accounts.values():
                writer.writerow([acct.account_id, acct.owner_name, acct.balance])

    def create_account(self, owner_name: str, starting_balance: float = 0.0) -> str:
        account_id = str(self._next_id)
        self._next_id += 1

        acct = Account(account_id, owner_name, starting_balance)
        self._accounts[account_id] = acct
        self._persist()
        return account_id

    def get_account(self, account_id: str) -> Account:
        try:
            return self._accounts[account_id]
        except KeyError:
            raise KeyError(f"Account {account_id!r} not found.")

    def deposit(self, account_id: str, amount: float):
        acct = self.get_account(account_id)
        acct.deposit(amount)
        self._persist()

    def withdraw(self, account_id: str, amount: float):
        acct = self.get_account(account_id)
        acct.withdraw(amount)
        self._persist()

    def transfer(self, from_id: str, to_id: str, amount: float):
        if from_id == to_id:
            raise ValueError("Cannot transfer to the same account.")
        # These calls each persist internally
        self.withdraw(from_id, amount)
        self.deposit(to_id, amount)

    def check_balance(self, account_id: str) -> float:
        """Return the current balance without modifying state."""
        acct = self.get_account(account_id)
        return acct.balance

    def load_from_csv(self, path: str):
        self._accounts.clear()
        self._next_id = 1
        with open(path, mode="r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                acct = Account(
                    account_id=row["account_id"],
                    owner_name=row["owner_name"],
                    balance=float(row["balance"])
                )
                self._accounts[acct.account_id] = acct
                self._next_id = max(self._next_id, int(acct.account_id) + 1)
