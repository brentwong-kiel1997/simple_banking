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

## Project Structure

```plaintext
simple_banking/
├── banking_system.py       # Core classes & auto-persistence logic
├── cli.py   # Optional command-line interface
├── test_banking_system.py  # pytest suite
└── tests/
    └── 
```



## Setup & Usage

### 1. Clone the repository:
```bash 
git clone https://github.com/brentwong-kiel1997/simple_banking
cd simple_banking
``` 

### 2. create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the banking system
```bash
python cli.py
```

### 5. Run tests
```bash
pytest tests/
```

**Important notes about pytest**

Depends on the IDE and venv setup. The `bank_test.py` file might need to be placed inside the `tests` folder to run properly.