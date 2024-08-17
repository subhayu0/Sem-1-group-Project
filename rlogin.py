import tkinter as tk
from tkinter import messagebox




# Create the main window
root = tk.Tk()
root.title("PursePal")
root.geometry("1920x1080")
root.configure(bg="#ECE4DB")

# Left Frame for image and text
left_frame = tk.Frame(root, bg="#5B3E3A")
left_frame.place(relwidth=0.5, relheight=1)

# Placeholder for image
canvas = tk.Canvas(left_frame, bg="#5B3E3A", bd=0, highlightthickness=0)
canvas.place(relwidth=1, relheight=0.6)
# Insert the actual image file location below
image = tk.PhotoImage(file="./pic.png")  # Replace with the actual image path
canvas.create_image(0, 0, anchor="nw", image=image)

# Text below the image
text = """No Cash!
No Card!
No Worries
We got You 👍
Welcome to PursePal 🙏"""
label_text = tk.Label(left_frame, text=text, bg="#5B3E3A", fg="#ECE4DB", font=("Helvetica", 14), justify="center")
label_text.place(relx=0.5, rely=0.75, anchor="center")

# Right Frame for login form
right_frame = tk.Frame(root, bg="#ECE4DB")
right_frame.place(relx=0.5, relwidth=0.5, relheight=1)

# PursePal Logo
logo_label = tk.Label(right_frame, text="PursePal", font=("Helvetica", 24), bg="#ECE4DB", fg="#5B3E3A")
logo_label.place(relx=0.1, rely=0.1)

def create_account():
    root.destroy()
    import test

# Create Account
create_account_button = tk.Button(right_frame, text="Create Purse Pal Account ➤", font=("Helvetica", 12), bg="#ECE4DB", fg="#5B3E3A", command=create_account)
create_account_button.place(relx=0.6, rely=0.1)
create_account_button.bind("<Button-1>")

# Login Form
login_label = tk.Label(right_frame, text="Login to PursePal", font=("Helvetica", 20), bg="#ECE4DB", fg="#5B3E3A")
login_label.place(relx=0.1, rely=0.3)

entry_mobile = tk.Entry(right_frame, font=("Helvetica", 14), width=30)
entry_mobile.insert(0, "Mobile or Email")
entry_mobile.place(relx=0.1, rely=0.4)

entry_password = tk.Entry(right_frame, font=("Helvetica", 14), width=30, show="*")
entry_password.insert(0, "Password")
entry_password.place(relx=0.1, rely=0.5)

forgot_password_label = tk.Label(right_frame, text="FORGOT PASSWORD?", font=("Helvetica", 10), bg="#ECE4DB", fg="#5B3E3A", cursor="hand2")
forgot_password_label.place(relx=0.55, rely=0.55)

def login():
    # Function to handle login click event
    mobile_or_email = entry_mobile.get()
    password = entry_password.get()
    # Check if the username and password are in the database. 
    
    if mobile_or_email and password:
        # Redirect the user to frontend. 
        root.destroy()
        import frontend
        frontend
    else:
        messagebox.showerror("Error", "Please enter both fields")


login_button = tk.Button(right_frame, text="Login", font=("Helvetica", 14), bg="#5B3E3A", fg="#ECE4DB", command=login)
login_button.place(relx=0.1, rely=0.6, relwidth=0.3)

# Start the Tkinter loop
root.mainloop()
