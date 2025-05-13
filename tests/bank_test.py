import os
import csv
import pytest
from banking_system import Bank

@pytest.fixture
def temp_csv(tmp_path):
    return str(tmp_path / "state.csv")

@pytest.fixture
def bank(temp_csv):
    return Bank(csv_path=temp_csv)

def read_state(csv_path):
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        return { (r["account_id"], r["owner_name"]): float(r["balance"])
                 for r in reader }

def test_create_and_balance(bank):
    acc = bank.create_account("Alice", 100.0)
    assert bank.check_balance(acc) == 100.0
    state = read_state(bank._csv_path)
    assert state[(acc, "Alice")] == 100.0

def test_deposit_and_balance(bank):
    acc = bank.create_account("Bob", 0.0)
    bank.deposit(acc, 25.0)
    assert bank.check_balance(acc) == 25.0
    state = read_state(bank._csv_path)
    assert state[(acc, "Bob")] == 25.0

def test_withdraw_and_balance(bank):
    acc = bank.create_account("Charlie", 50.0)
    bank.withdraw(acc, 20.0)
    assert bank.check_balance(acc) == 30.0
    state = read_state(bank._csv_path)
    assert state[(acc, "Charlie")] == 30.0

def test_overdraft_raises_and_no_change(bank):
    acc = bank.create_account("Dave", 10.0)
    with pytest.raises(ValueError):
        bank.withdraw(acc, 20.0)
    # Balance remains
    assert bank.check_balance(acc) == 10.0
    state = read_state(bank._csv_path)
    assert state[(acc, "Dave")] == 10.0

def test_transfer_and_balances(bank):
    a = bank.create_account("Eve", 200.0)
    b = bank.create_account("Frank", 50.0)
    bank.transfer(a, b, 100.0)
    assert bank.check_balance(a) == 100.0
    assert bank.check_balance(b) == 150.0
    state = read_state(bank._csv_path)
    assert state[(a, "Eve")] == 100.0
    assert state[(b, "Frank")] == 150.0

def test_load_existing_and_next_id(tmp_path):
    # Pre-create CSV
    csv_path = tmp_path / "pre.csv"
    rows = [
        ["account_id","owner_name","balance"],
        ["1","Gina","300.0"],
        ["2","Hank","150.5"]
    ]
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    bank2 = Bank(csv_path=str(csv_path))
    # Loaded correctly
    assert bank2.check_balance("1") == 300.0
    assert bank2.check_balance("2") == 150.5
    # Next ID is 3
    new_id = bank2.create_account("Ivy", 0.0)
    assert new_id == "3"
