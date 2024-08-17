import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
 
# Function to connect to SQLite and create the transactions table if it doesn't exist
def create_db():
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_name TEXT,
            amount REAL
        )
    ''')
    conn.commit()
    conn.close()
 
# Function to insert a new transaction into the database
def insert_transaction(name, amount):
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (transaction_name, amount) VALUES (?, ?)", (name, amount))
    conn.commit()
    conn.close()
    refresh_transactions()  # Refresh the GUI after inserting
 
# Function to update a transaction in the database
def update_transaction(transaction_id, new_name, new_amount):
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE transactions SET transaction_name = ?, amount = ? WHERE id = ?", (new_name, new_amount, transaction_id))
    conn.commit()
    conn.close()
    refresh_transactions()  # Refresh the GUI after updating
 
# Function to delete a transaction from the database
def delete_transaction(transaction_id):
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()
    refresh_transactions()  # Refresh the GUI after deletion
 
# Function to fetch all transactions from the database
def fetch_transactions():
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, transaction_name, amount FROM transactions")
    rows = cursor.fetchall()
    conn.close()
    return rows
 
# Function to populate the list of transactions in the GUI
def populate_transactions():
    transactions = fetch_transactions()
    for transaction in transactions:
        tree.insert("", "end", values=(transaction[0], transaction[1], f"{transaction[2]:+.2f}"))
 
# Function to refresh the list of transactions in the GUI
def refresh_transactions():
    tree.delete(*tree.get_children())  # Clear the Treeview
    populate_transactions()  # Repopulate it with updated data
 
# Function to handle selecting a transaction
def on_select(event):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        transaction_id, transaction_name, amount = item["values"]
        transaction_id_var.set(transaction_id)
        transaction_name_var.set(transaction_name)
        amount_var.set(amount)
 
# Function to handle adding a transaction
def on_add():
    new_name = transaction_name_entry.get()
    try:
        new_amount = float(amount_entry.get())
        if new_name:
            insert_transaction(new_name, new_amount)
            messagebox.showinfo("Success", "Transaction added successfully!")
        else:
            messagebox.showwarning("Error", "Please enter a transaction name!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount!")
 
# Function to handle updating a transaction
def on_update():
    try:
        transaction_id = transaction_id_var.get()
        new_name = transaction_name_entry.get()
        new_amount = float(amount_entry.get())
        if transaction_id and new_name and new_amount:
            update_transaction(transaction_id, new_name, new_amount)
            messagebox.showinfo("Success", "Transaction updated successfully!")
        else:
            messagebox.showwarning("Error", "Please fill out all fields!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount!")
 
# Function to handle deleting a transaction
def on_delete():
    transaction_id = transaction_id_var.get()
    if transaction_id:
        delete_transaction(transaction_id)
        messagebox.showinfo("Success", "Transaction deleted successfully!")
    else:
        messagebox.showwarning("Error", "Please select a transaction to delete!")
 
# Main window setup
root = tk.Tk()
root.title("Purse Pal")
root.geometry("800x600")
 
# Create left-side navigation
nav_frame = tk.Frame(root, bg="brown")
nav_frame.pack(side="left", fill="y")
 
# Add labels for navigation options
home_label = tk.Label(nav_frame, text="HOME", font=("Arial", 16), bg="brown", fg="white")
home_label.pack(pady=10)
 
statement_label = tk.Label(nav_frame, text="STATEMENT", font=("Arial", 16), bg="brown", fg="white")
statement_label.pack(pady=10)
 
contact_label = tk.Label(nav_frame, text="CONTACT", font=("Arial", 16), bg="brown", fg="white")
contact_label.pack(pady=10)
 
settings_label = tk.Label(nav_frame, text="SETTINGS", font=("Arial", 16), bg="brown", fg="white")
settings_label.pack(pady=10)
 
# Main content frame for transaction list
main_frame = tk.Frame(root)
main_frame.pack(side="right", fill="both", expand=True)
 
# Add a title for the main frame
title_label = tk.Label(main_frame, text="RECENT TRANSACTIONS", font=("Arial", 24), fg="brown")
title_label.pack(pady=20)
 
# Create a Treeview widget to display transactions
columns = ("ID", "Transaction", "Amount")
tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=10)
 
# Define headings
tree.heading("ID", text="ID")
tree.heading("Transaction", text="Transaction")
tree.heading("Amount", text="Amount")
 
# Define column widths
tree.column("ID", width=50, anchor="center")
tree.column("Transaction", width=400, anchor="w")
tree.column("Amount", width=100, anchor="center")
 
# Add treeview to the main frame
tree.pack(fill="both", expand=True)
 
# Bind the treeview selection event
tree.bind("<<TreeviewSelect>>", on_select)
 
# Form for adding/updating transactions
form_frame = tk.Frame(main_frame)
form_frame.pack(pady=20)
 
transaction_id_var = tk.IntVar()
transaction_name_var = tk.StringVar()
amount_var = tk.StringVar()
 
tk.Label(form_frame, text="Transaction ID (Auto):").grid(row=0, column=0)
transaction_id_entry = tk.Entry(form_frame, textvariable=transaction_id_var, state='readonly')
transaction_id_entry.grid(row=0, column=1)
 
tk.Label(form_frame, text="Transaction Name:").grid(row=1, column=0)
transaction_name_entry = tk.Entry(form_frame, textvariable=transaction_name_var)
transaction_name_entry.grid(row=1, column=1)
 
tk.Label(form_frame, text="Amount:").grid(row=2, column=0)
amount_entry = tk.Entry(form_frame, textvariable=amount_var)
amount_entry.grid(row=2, column=1)
 
add_button = tk.Button(form_frame, text="Add Transaction", command=on_add)
add_button.grid(row=3, column=0, pady=10)
 
update_button = tk.Button(form_frame, text="Update Transaction", command=on_update)
update_button.grid(row=3, column=1, pady=10)
 
delete_button = tk.Button(form_frame, text="Delete Transaction", command=on_delete)
delete_button.grid(row=3, column=2, pady=10)
 
# Initialize the database and populate with mock data
create_db()
 
# Populate the Treeview with data
refresh_transactions()
 
# Start the Tkinter main loop
root.mainloop()