import tkinter as tk
from tkinter import messagebox
 
def send_money():
    pursepal_id = pursepal_id_entry.get()
    amount = amount_entry.get()
    purpose = purpose_entry.get()
    remarks = remarks_entry.get()
 
    if not pursepal_id or not amount or not purpose or not remarks:
        messagebox.showerror("Error", "All fields are required.")
        return
 
    # Handle the sending money functionality here
    messagebox.showinfo("Success", f"Money sent to {pursepal_id} successfully!")
 
# Initialize the main window
root = tk.Tk()
root.title("Send Money")
root.geometry("550x500")
root.config(bg='#f4f3f1')
 
# Send Money Label
send_money_label = tk.Label(root, text="Send Money", font=('Jacques Francois', 24), fg='#4b2e2a', bg='#f4f3f1')
send_money_label.pack(pady=20)
 
# Common settings for entry fields
entry_settings = {
    'font': ('Jacques Francois', 14),
    'fg': '#4b2e2a',
    'bg': '#f4f3f1',
    'relief': 'solid',
    'borderwidth': 1,
    'highlightthickness': 0,
    'insertbackground': '#4b2e2a',
    'cursor': 'xterm',
    'width': 40  # Adjust the width
}
 
# Frame to contain the form elements
form_frame = tk.Frame(root, bg='#f4f3f1')
form_frame.pack(padx=20, pady=20)
 
# PursePal ID Entry
pursepal_id_label = tk.Label(form_frame, text="PursePal Id (mobile/email)", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1')
pursepal_id_label.grid(row=0, column=0, sticky='w', pady=(0, 10))
pursepal_id_entry = tk.Entry(form_frame, **entry_settings)
pursepal_id_entry.grid(row=1, column=0, pady=(0, 10))
 
# Amount Entry
amount_label = tk.Label(form_frame, text="Amount", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1')
amount_label.grid(row=2, column=0, sticky='w', pady=(0, 10))
amount_entry = tk.Entry(form_frame, **entry_settings)
amount_entry.grid(row=3, column=0, pady=(0, 10))
 
# Purpose Entry
purpose_label = tk.Label(form_frame, text="Purpose", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1')
purpose_label.grid(row=4, column=0, sticky='w', pady=(0, 10))
purpose_entry = tk.Entry(form_frame, **entry_settings)
purpose_entry.grid(row=5, column=0, pady=(0, 10))
 
# Remarks Entry (larger entry box)
remarks_label = tk.Label(form_frame, text="Remarks", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1')
remarks_label.grid(row=6, column=0, sticky='w', pady=(0, 10))
remarks_entry = tk.Entry(form_frame, **entry_settings)  # Larger width for Remarks
remarks_entry.grid(row=7, column=0, pady=(0, 10), ipady=20)  # Increased ipady to make it taller
 
# Send Button
send_button = tk.Button(root, text="Send", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', borderwidth=1, relief='solid', command=send_money)
send_button.pack(pady=20)
 
# Run the application
root.mainloop()
