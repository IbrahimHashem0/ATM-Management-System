import pymysql
from tkinter import messagebox

def get_connection():
    try:
        return pymysql.connect(
            host="127.0.0.1",
            user="root",
            passwd="0642&0825&Ii",
            database="ATM"
        )
    except pymysql.MySQLError as e:
        messagebox.showerror("DB Error", f"Cannot connect to database: {e}")
        return None
