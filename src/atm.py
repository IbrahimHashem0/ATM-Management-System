import tkinter as tk
from tkinter import ttk, messagebox
from transaction import TransactionHistory
from db import get_connection

class atm():
    def __init__(self, root):
        self.root = root
        self.root.title("ATM IH Bank")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title = tk.Label(self.root, text="ATM Machine IH Bank", bd=4, relief="groove", bg="light green",
                         font=("Arial", 50, "bold"))
        title.pack(side="top", fill="x")

        self.history = TransactionHistory()
        self.create_option_frame()

        # ===== Detail Frame =====
        self.detFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(240, 180, 150))
        self.detFrame.place(width=self.width / 2, height=self.height - 180, x=self.width / 3 + 140, y=100)
        lbl = tk.Label(self.detFrame, text="Account Details", bd=3, font=("Arial", 30, "bold"),
                       bg=self.clr(230, 210, 155))
        lbl.pack(side="top", fill="x")

        # ===== Table
        self.tabFun()

    # ===== Option Frame =====
    def create_option_frame(self):
        optFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(160, 200, 250))
        optFrame.place(width=self.width / 3, height=self.height - 180, x=70, y=100)

        tk.Label(optFrame, text="Atm_Card:", bg=self.clr(160, 200, 250), font=("Arial", 15, "bold")).grid(row=0, column=0, padx=20, pady=30)
        self.atm = tk.Entry(optFrame, width=20, font=("Arial", 15), bd=2)
        self.atm.grid(row=0, column=1, padx=10, pady=30)

        tk.Label(optFrame, text="Password:", bg=self.clr(160, 200, 250), font=("Arial", 15, "bold")).grid(row=1, column=0, padx=20, pady=30)
        self.pw = tk.Entry(optFrame, width=20, font=("Arial", 15), bd=2, show="*")
        self.pw.grid(row=1, column=1, padx=10, pady=30)

        tk.Button(optFrame, command=self.inqFun, text="Balance Inquiry", width=15, bd=2, relief="raised", font=("Arial", 12, "bold")).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(optFrame, command=self.frameFun, text="Cash Withdraw", width=15, bd=2, relief="raised", font=("Arial", 12, "bold")).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(optFrame, command=self.transFrame, text="Transaction", width=15, bd=2, relief="raised", font=("Arial", 12, "bold")).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(optFrame, command=self.showHistory, text="Show History", width=15, bd=2, relief="raised", font=("Arial", 12, "bold")).grid(row=5, column=0, columnspan=2, pady=10)

    # ===== Table Function =====
    # ===== Table Function =====
    def tabFun(self, history_mode=False):
        if hasattr(self, 'table'):
            self.table.destroy()
        tabFrame = tk.Frame(self.detFrame, bd=4, relief="sunken", bg="cyan")
        tabFrame.place(width=self.width / 2 - 40, height=self.height - 270, x=17, y=70)

        x_scrol = tk.Scrollbar(tabFrame, orient="horizontal")
        x_scrol.pack(side="bottom", fill="x")
        y_scrol = tk.Scrollbar(tabFrame, orient="vertical")
        y_scrol.pack(side="right", fill="y")

        if history_mode:  # وضع التاريخ
            self.table = ttk.Treeview(tabFrame, xscrollcommand=x_scrol.set, yscrollcommand=y_scrol.set,
                                      columns=("acc", "action", "amount", "balance", "timestamp"))
            self.table.heading("acc", text="Account_No")
            self.table.heading("action", text="Action")
            self.table.heading("amount", text="Amount")
            self.table.heading("balance", text="Balance")
            self.table.heading("timestamp", text="Time")
        else:
            self.table = ttk.Treeview(tabFrame, xscrollcommand=x_scrol.set, yscrollcommand=y_scrol.set,
                                      columns=("ac", "name", "bal"))
            self.table.heading("ac", text="Account_No")
            self.table.heading("name", text="User_Name")
            self.table.heading("bal", text="Balance")

        x_scrol.config(command=self.table.xview)
        y_scrol.config(command=self.table.yview)
        self.table["show"] = "headings"
        self.table.pack(fill="both", expand=1)

    # ===== Show Transaction History =====
    def showHistory(self):
        hist = self.history.get_history()
        if not hist:
            messagebox.showinfo("History", "No transactions yet")
            return
        self.tabFun(history_mode=True)  # نفتح الجدول بوضع التاريخ
        self.table.delete(*self.table.get_children())
        for h in hist:
            self.table.insert('', tk.END, values=h)

    # ===== DB Connection =====
    def dbFun(self):
        self.con = get_connection()
        if self.con:
            self.cur = self.con.cursor()
        else:
            raise Exception("Database connection failed")

    # ===== Balance Inquiry =====
    def inqFun(self):
        atm_val = self.atm.get()
        pw_val = self.pw.get()
        try:
            atmNo, pw = int(atm_val), int(pw_val)
        except ValueError:
            messagebox.showerror("Error", "ATM & Password must be numeric")
            return
        try:
            self.dbFun()
            self.cur.execute("select password from atm where atmNo=%s", (atmNo,))
            password = self.cur.fetchone()
            if password and pw == password[0]:
                self.cur.execute("select accountNo, name, balance from atm where atmNo=%s", (atmNo,))
                data = self.cur.fetchone()
                self.table.delete(*self.table.get_children())
                self.table.insert('', tk.END, values=data)
            elif not password:
                messagebox.showerror("Error", "Invalid Atm_No")
            else:
                messagebox.showerror("Error", "Invalid Password")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
        finally:
            if hasattr(self, "con") and self.con:
                self.con.close()

    # ===== Cash Withdraw =====
    def frameFun(self):
        self.amountFrame = tk.Frame(self.root, bd=4, relief="ridge", bg=self.clr(150, 240, 220))
        self.amountFrame.place(width=self.width / 3, height=250, x=self.width / 3 + 120, y=100)

        tk.Label(self.amountFrame, text="Amount:", bg=self.clr(150, 240, 220), font=("Arial", 15, "bold")).grid(row=0, column=0, padx=20, pady=30)
        self.wdIn = tk.Entry(self.amountFrame, width=20, bd=2, font=("Arial", 15))
        self.wdIn.grid(row=0, column=1, padx=10, pady=30)

        tk.Button(self.amountFrame, command=self.wdFun, text="Enter", bd=3, relief="raised",
                  font=("Arial", 20, "bold"), width=20).grid(row=1, column=0, padx=30, pady=40, columnspan=2)

    def wdFun(self):
        atm_val = self.atm.get()
        pw_val = self.pw.get()
        amt_val = self.wdIn.get()
        try:
            atmNo, pw, amount = int(atm_val), int(pw_val), int(amt_val)
        except ValueError:
            messagebox.showerror("Error", "ATM, Password & Amount must be numeric")
            return
        if amount <= 0:
            messagebox.showerror("Error", "Amount must be greater than 0")
            return
        try:
            self.dbFun()
            self.cur.execute("select password, balance from atm where atmNo=%s", (atmNo,))
            info = self.cur.fetchone()
            if info:
                if pw == info[0]:
                    if amount <= info[1]:
                        if messagebox.askyesno("Confirm", f"Withdraw {amount}?"):
                            new_balance = info[1] - amount
                            self.cur.execute("update atm set balance=%s where atmNo=%s", (new_balance, atmNo))
                            try:
                                self.con.commit()
                            except:
                                self.con.rollback()
                            self.history.add_transaction(atmNo, "withdraw", amount, new_balance)
                            messagebox.showinfo("Success", "Operation was successful")
                            self.inqFun()
                    else:
                        messagebox.showerror("Error", "Insufficient balance")
                else:
                    messagebox.showerror("Error", "Invalid Password")
            else:
                messagebox.showerror("Error", "Invalid Atm_No")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
        finally:
            self.desFrame()
            if hasattr(self, "con") and self.con:
                self.con.close()

    def desFrame(self):
        if hasattr(self, 'amountFrame'):
            self.amountFrame.destroy()

    # ===== Transaction Transfer =====
    def transFrame(self):
        self.transFrame = tk.Frame(self.root, bd=4, relief="ridge", bg=self.clr(150, 240, 220))
        self.transFrame.place(width=self.width / 3, height=350, x=self.width / 3 + 120, y=100)

        tk.Label(self.transFrame, text="Amount:", bg=self.clr(150, 240, 220), font=("Arial", 15, "bold")).grid(row=0, column=0, padx=20, pady=30)
        self.transIn = tk.Entry(self.transFrame, width=20, bd=2, font=("Arial", 15))
        self.transIn.grid(row=0, column=1, padx=10, pady=30)

        tk.Label(self.transFrame, text="Account_No:", bg=self.clr(150, 240, 220), font=("Arial", 15, "bold")).grid(row=1, column=0, padx=20, pady=30)
        self.user2In = tk.Entry(self.transFrame, width=20, bd=2, font=("Arial", 15))
        self.user2In.grid(row=1, column=1, padx=10, pady=30)

        tk.Button(self.transFrame, command=self.transFun, text="Enter", bd=3, relief="raised",
                  font=("Arial", 20, "bold"), width=20).grid(row=2, column=0, padx=30, pady=40, columnspan=2)

    def desTrans(self):
        if hasattr(self, 'transFrame'):
            self.transFrame.destroy()

    def transFun(self):
        atm_val = self.atm.get()
        pw_val = self.pw.get()
        receiver_val = self.user2In.get()
        amount_val = self.transIn.get()
        try:
            atmNo, pw, user2, amount = int(atm_val), int(pw_val), int(receiver_val), int(amount_val)
        except ValueError:
            messagebox.showerror("Error", "All fields must be numeric")
            return
        if amount <= 0:
            messagebox.showerror("Error", "Amount must be greater than 0")
            return
        try:
            self.dbFun()
            self.cur.execute("select password, balance from atm where atmNo=%s", (atmNo,))
            info = self.cur.fetchone()
            if info:
                if pw == info[0]:
                    if amount <= info[1]:
                        self.cur.execute("select balance from atm where accountNo=%s", (user2,))
                        receiver = self.cur.fetchone()
                        if receiver:
                            if messagebox.askyesno("Confirm", f"Transfer {amount} to account {user2}?"):
                                new_balance = info[1] - amount
                                receiver_new = receiver[0] + amount
                                self.cur.execute("update atm set balance=%s where atmNo=%s", (new_balance, atmNo))
                                self.cur.execute("update atm set balance=%s where accountNo=%s", (receiver_new, user2))
                                try:
                                    self.con.commit()
                                except:
                                    self.con.rollback()
                                self.history.add_transaction(atmNo, "transfer", amount, new_balance)
                                messagebox.showinfo("Success", "Operation was successful")
                                self.inqFun()
                        else:
                            messagebox.showerror("Error", "Receiver account not found")
                    else:
                        messagebox.showerror("Error", "Insufficient balance")
                else:
                    messagebox.showerror("Error", "Invalid Password")
            else:
                messagebox.showerror("Error", "Invalid Atm_No")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
        finally:
            self.desTrans()
            if hasattr(self, "con") and self.con:
                self.con.close()

    # ===== Show Transaction History =====
    def showHistory(self):
        hist = self.history.get_history()
        if not hist:
            messagebox.showinfo("History", "No transactions yet")
            return
        self.tabFun(history_mode=True)  # يجب فتح الجدول مع التاريخ
        self.table.delete(*self.table.get_children())
        for h in hist:
            self.table.insert('', tk.END, values=h)

    # ===== Color Helper =====
    def clr(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"
