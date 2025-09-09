# ATM Management System (Python)

## Overview
This ATM Management System is a GUI-based Python application using Tkinter and MySQL, designed to simulate a real-world ATM system.  
It allows users to manage accounts, perform transactions, and track transaction history efficiently using Object-Oriented Programming (OOP) principles.

## Features
- **User Authentication**: Secure login using ATM card number and password with numeric validation.  
- **Balance Inquiry**: Check current account balance instantly.  
- **Cash Withdrawal**: Withdraw cash with validation for sufficient balance.  
- **Money Transfer**: Transfer funds to other accounts safely with confirmation prompts.  
- **Transaction History**: Maintains a full history of withdrawals and transfers using a linked list.  
- **Input Validation**: Ensures numeric input for ATM number, password, account number, and transaction amounts.  
- **Optimized Data Handling**: 
  - Accounts stored in Python `dict` (via MySQL DB queries) for fast lookup.  
  - Transaction history managed with a linked list for efficient insertion and retrieval.

## Technologies & Concepts Used
- **Programming Language**: Python 3.x  
- **GUI Library**: Tkinter  
- **Database**: MySQL (via `pymysql`)  
- **OOP Principles**: Encapsulation, modularity  
- **Data Structures & Algorithms**:  
  - Linked List for transaction history  
  - `any()` and `all()` for input validation  
- **IDE Tested On**: PyCharm, VSCode

## Installation
1. Clone the repository:  
`git clone https://github.com/IbrahimHashem0/ATM-Management-System-Python.git`
2. Navigate to the project folder:  
`cd ATM-Management-System-Python`
3. Install dependencies:  
`pip install -r requirements.txt`
4. Set up the MySQL database:
   - Database name: `ATM`  
   - Table: `atm` with columns `atmNo`, `password`, `accountNo`, `name`, `balance`
5. Run the application:  
`python main.py`

## Usage
Run the program and use the GUI menu:
- Enter ATM number and password to login
- Check Balance
- Withdraw Cash
- Transfer Money
- View Transaction History
- Exit

**Notes:**
- All operations validate input and account balance.  
- Transaction history is displayed chronologically.  
- Each transaction is stored in the linked list for easy retrieval.

## Future Improvements
- Add deposit functionality.  
- Implement user registration with account creation.  
- Enhance GUI with advanced features, themes, and charts.  
- Support multi-user concurrency for networked ATM operations.  
- Mobile app integration for remote account management.

## License
This project is open-source under the MIT License.
