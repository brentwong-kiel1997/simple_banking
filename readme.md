# Simple Banking System

A minimal, console-based banking system in Python with the following features:

- **Account Management**  
  - Create new accounts with a unique ID, owner name, and starting balance  
  - Check current balance  

- **Transactions & Constraints**  
  - Deposit and withdraw funds (no negative amounts)  
  - Prevent overdrafts (withdrawals or transfers that exceed balance raise an error)  
  - Transfer money between accounts in the same bank  

- **Automatic Save**  
  - On each account creation or transaction, the entire system state is saved to `bank_state.csv`  
  - On startup, existing state (if any) is loaded automatically  

- **Test Coverage**  
  - Comprehensive tests using [pytest](https://docs.pytest.org/)  
  - Covers account creation, deposits, withdrawals, transfers, balance checks, persistence, and edge cases  

---

## 📁 Project Structure

```plaintext
simple_banking/
├── banking_system.py       # Core classes & auto-persistence logic
├── cli.py                  # Optional command-line interface
└── tests/
    └── test_banking_system.py  # pytest suite
```



