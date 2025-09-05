# ATM Management System



###### ATM IH Bank is a desktop-based Python application with a GUI, designed to simulate a real-world ATM system. It allows users to manage accounts, perform transactions, and track transaction history efficiently.



#### 

### Features



##### User Authentication:



Secure login using ATM card number and password.



Numeric validation ensures only valid input is accepted.



###### Balance Inquiry:



Check current account balance instantly.



Retrieves data from a MySQL database in real-time.



###### Cash Withdrawal:



Withdraw cash in user-specified amounts.



Validates sufficient balance before completing transactions.



Records each withdrawal in the transaction history.



###### Money Transfer:



Transfer funds to other accounts using account numbers.



Confirms transaction with a pop-up prompt before execution.



Updates sender and receiver balances atomically.



###### Transaction History:



Maintains a full history of transactions using a linked list.



Shows date and time for each operation.



Displays all withdrawals and transfers chronologically in the GUI.



###### GUI Interface:



Interactive and responsive GUI using Tkinter.



Scrollable tables for account details and transaction history.



Color-coded frames for better user experience.



#### Technical Highlights



###### Data Structures \& Algorithms:



Linked List: Stores transaction history efficiently with O(1) insertion.



Tkinter Treeview: Displays account and transaction data in tabular format.



Input validation ensures numeric values for ATM, password, and amount.



###### Database Management:



MySQL: Stores account information including ATM number, password, account number, and balance.



Supports real-time updates and retrieval with secure SQL queries.



Object-Oriented Programming (OOP):



Encapsulated classes for ATM, Transaction History, and Transactions.



Modular design allows easy extension for new features like deposit or bill payment.



###### User Interaction \& Safety:



Confirmation prompts before withdrawals and transfers.



Prevents overdraft by validating balance before transactions.



Displays meaningful error messages for invalid inputs or failed operations.



#### Numbers \& Performance



Supports multiple accounts (limited only by database size).



Transaction history stores an unlimited number of transactions using linked list.



GUI can display hundreds of rows of account or transaction data with smooth scrolling.



Typical operations (balance check, withdrawal, transfer) execute in O(1) database queries plus minor GUI rendering time.



#### Future Improvements



Add deposit functionality.



Integrate user registration and login with account creation.



Enhance GUI with advanced themes and charts for spending analysis.



Implement real-time multi-user concurrency for networked ATM operations.



Support mobile app integration for remote account management.

