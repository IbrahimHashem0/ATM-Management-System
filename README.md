# ATM Management System

## Overview
This ATM Management System is a console-based C++ application designed to simulate a real-world ATM system.  
It allows users to manage accounts, perform transactions, and track transaction history efficiently using modular design and Object-Oriented Programming (OOP) principles.

## Features
- **User Authentication**: Secure login using ATM card number and password with input validation.  
- **Balance Inquiry**: Check current account balance instantly.  
- **Cash Withdrawal**: Withdraw cash with validation for sufficient balance.  
- **Money Transfer**: Transfer funds to other accounts safely with confirmation prompts.  
- **Transaction History**: Maintains a full history of withdrawals and transfers using a linked list.  
- **Input Validation**: Ensures numeric input for ATM number, password, and transaction amounts.  
- **Optimized Data Handling**: 
  - Accounts stored in `std::unordered_map` for O(1) lookup.  
  - Transaction history managed with a linked list for efficient insertion and traversal.

## Technologies & Concepts Used
- **Programming Language**: C++  
- **OOP Principles**: Encapsulation, modularity  
- **Data Structures & Algorithms**:  
  - `std::unordered_map` for fast account lookup  
  - Linked List for transaction history  
  - `std::find`, `std::all_of` for validation  
- **Build System**: CMake  
- **IDE Tested On**: CLion

## Installation
1. Clone the repository:  
`git clone https://github.com/IbrahimHashem0/ATM-Management-System.git`
2. Navigate to the project folder:  
`cd ATM-Management-System`
3. Create a build directory and compile:  
`mkdir build`  
`cd build`  
`cmake ..`  
`cmake --build .`
4. Run the application:  
`./ATM_Management_System`  *(On Windows: ATM_Management_System.exe)*

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
