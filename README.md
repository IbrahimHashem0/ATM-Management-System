# ATM Management System (Python)

## Overview
This ATM Management System is a console-based Python application designed to simulate a real-world ATM system.  
It allows users to manage accounts, perform transactions, and track transaction history efficiently using modular design and Object-Oriented Programming (OOP) principles.

## Features
- **User Authentication**: Secure login using ATM card number and password with input validation.  
- **Balance Inquiry**: Check current account balance instantly.  
- **Cash Withdrawal**: Withdraw cash with validation for sufficient balance.  
- **Money Transfer**: Transfer funds to other accounts safely with confirmation prompts.  
- **Transaction History**: Maintains a full history of withdrawals and transfers using a linked list or Python list.  
- **Input Validation**: Ensures numeric input for ATM number, password, and transaction amounts.  
- **Optimized Data Handling**: 
  - Accounts stored in Python `dict` for O(1) lookup.  
  - Transaction history managed with `list` for efficient insertion and traversal.

## Technologies & Concepts Used
- **Programming Language**: Python 3.x  
- **OOP Principles**: Encapsulation, modularity  
- **Data Structures & Algorithms**:  
  - `dict` for fast account lookup  
  - `list` for transaction history  
  - `any()`, `all()` for input validation  
- **GUI (optional)**: Tkinter  
- **IDE Tested On**: PyCharm, VSCode

## Installation
1. Clone the repository:  
`git clone https://github.com/IbrahimHashem0/ATM-Management-System-Python.git`
2. Navigate to the project folder:  
`cd ATM-Management-System-Python`
3. Install dependencies (if GUI is used):  
`pip install -r requirements.txt`
4. Run the application:  
`python atm_system.py`

## Usage
Run the program and follow the console menu:
- Login with ATM number and password
- Check Balance
- Withdraw Cash
- Transfer Money
- View Transaction History
- Exit

**Notes:**
- All operations validate input and account balance.  
- Transaction history records each withdrawal and transfer in chronological order.

## Future Improvements
- Add deposit functionality.  
- Integrate user registration with account creation.  
- Enhance GUI with advanced features and themes.  
- Implement multi-user concurrency for networked ATM operations.  
- Support mobile app integration for remote account management.

## License
This project is open-source under the MIT License.
