from datetime import datetime

# ====== DSA: Transaction History using Linked List ======
class TransactionNode:
    def __init__(self, acc_no, action, amount, balance, timestamp=None):
        self.acc_no = acc_no
        self.action = action  # "withdraw", "deposit", "transfer"
        self.amount = amount
        self.balance = balance
        self.timestamp = timestamp if timestamp else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.next = None

class TransactionHistory:
    def __init__(self):
        self.head = None

    def add_transaction(self, acc_no, action, amount, balance):
        new_node = TransactionNode(acc_no, action, amount, balance)
        new_node.next = self.head
        self.head = new_node

    def get_history(self):
        history_list = []
        current = self.head
        while current:
            history_list.append((current.acc_no, current.action, current.amount, current.balance, current.timestamp))
            current = current.next
        return history_list[::-1]  # oldest first
