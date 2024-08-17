import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import sqlite3 as sql

def make_circle_image(image_path, size):
    # Open the image and resize it
    image = Image.open(image_path).resize((size, size), Image.LANCZOS)
    
    # Create a circular mask
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    
    # Apply the mask to the image
    circular_image = Image.new("RGBA", (size, size))
    circular_image.paste(image, (0, 0), mask=mask)
    
    return ImageTk.PhotoImage(circular_image)

def on_closing():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Purse Pal Registration")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.attributes('-fullscreen', False)

# Left frame for the image and text
left_frame = tk.Frame(root, bg='#4b2e2a')
left_frame.pack(side='left', fill='both', expand=True)

# Load and display the circular image
image_path = "./pic2.1.webp"
photo = make_circle_image(image_path, 500)

image_label = tk.Label(left_frame, image=photo, bg='#4b2e2a')
image_label.image = photo
image_label.pack(pady=20)

# Text under the image
text_label = tk.Label(left_frame, text="No Cash!\nNo Card!\nNo Worries\nWe got You 👍\nWelcome to PursePal 🙏", fg='white', bg='#4b2e2a', font=('Helvetica', 16))
text_label.pack(pady=20)

# Right frame for the form
right_frame = tk.Frame(root, bg='#f4f3f1')
right_frame.pack(side='right', fill='both', expand=True)

# Load and display the logo image
logo_path = "./pursepal_logo.jpeg"
logo_image = Image.open(logo_path).resize((100, 100), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(right_frame, image=logo_photo, bg='#f4f3f1')
logo_label.image = logo_photo
logo_label.pack(anchor='ne', padx=20, pady=20)

# "Register" text
register_label = tk.Label(right_frame, text="Register", font=('Helvetica', 24), fg='#4b2e2a', bg='#f4f3f1')
register_label.pack(anchor='n', pady=(20, 10))

def goto_login(): 
    root.destroy()
    import rlogin

# Go to Login link
login_link = tk.Button(right_frame, text="Go to Login ▸", font=('Helvetica', 12), fg='#4b2e2a', bg='#f4f3f1', command=goto_login)
login_link.pack(anchor='ne', padx=20, pady=20)

# Registration form
form_frame = tk.Frame(right_frame, bg='#f4f3f1')
form_frame.pack(pady=20, padx=50)

# Function to create form entries
def create_form_entry(label_text, type="text"):
    label = tk.Label(form_frame, text=label_text, font=('Helvetica', 14), fg='#4b2e2a', bg='#f4f3f1')
    label.pack(anchor='w', pady=5)
    entry = tk.Entry(form_frame, font=('Helvetica', 14), fg='#4b2e2a', bg='#f4f3f1', highlightthickness=0, relief='flat', bd=0)
    entry.pack(fill='x', pady=5)
    line = tk.Frame(form_frame, height=2, bg='#4b2e2a')
    line.pack(fill='x', pady=(0, 20))
    return entry

# Form fields
full_name = create_form_entry("Full Name")
email_address = create_form_entry("Email") 
mobile_number  = create_form_entry("Mobile Number")
date_of_birth = create_form_entry("Date of Birth")

# Gender selection
gender_label = tk.Label(form_frame, text="Gender", font=('Helvetica', 14), fg='#4b2e2a', bg='#f4f3f1')
gender_label.pack(anchor='w', pady=5)
gender_frame = tk.Frame(form_frame, bg='#f4f3f1')
gender_frame.pack(anchor='w', pady=5)

genders = ["Male", "Female", "Other"]
gender_var = tk.StringVar(value=0)

for gender in genders:
    rb = tk.Radiobutton(gender_frame, text=gender, variable=gender_var, value=gender, font=('Helvetica', 14), fg='#4b2e2a', bg='#f4f3f1', selectcolor='#f4f3f1')
    rb.pack(side='left', padx=10)

# Password fields
password_1 = create_form_entry("Password", type="password")
password_2 = create_form_entry("Confirm Password", type="password")

def on_join_click():
    # create a database if it is not there. 
    
    #connect to the database. 
    db = sql.connect("user.sqlite3")
    cursor = db.cursor()

    name = full_name.get()
    email = email_address.get()
    password = password_1.get() 
    number = mobile_number.get()
    dob = date_of_birth.get()
    
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS APP_USER (id INTEGER PRIMARY KEY AUTOINCREMENT,  full_name  TEXT NOT NULL, email_address TEXT NOT NULL, mobile_number TEXT NOT NULL, date_of_birth TEXT NOT NULL,  password TEXT NOT NULL)"
        )
    
    # Perform some validation. 
    print(name)
    print(email)
    print(number)
    print(dob)
    print(password)
    # Instead of printing, store this in the database.
    
    # Store the valid data in the database
    cursor.execute("INSERT INTO APP_USER (full_name, email_address, mobile_number, date_of_birth, password) VALUES (?, ?, ?, ?, ?)", (name, email, number, dob, password))

    # Commit the transaction
    db.commit()

    # Close the connection
    db.close()
    

# Join button
join_button = tk.Button(form_frame, text="Join", font=('Helvetica', 14), fg='#4b2e2a', bg='#f4f3f1', borderwidth=0, command=on_join_click)

join_button.pack(pady=20)

# Run the application
root.mainloop()
