import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Initialize main window
root = tk.Tk()
root.title("Purse Pal Dashboard")
root.geometry("1200x800")
root.configure(bg='#5D2E2E')  # Background color for the main window

# Load the Purse Pal logo image
logo_path = './pursepal_logo.jpeg'  # Replace with your image path
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((100, 100), Image.LANCZOS)  # Resize image if needed
logo = ImageTk.PhotoImage(logo_image)

# Header Section
header_frame = tk.Frame(root, bg='#5D2E2E')
header_frame.pack(fill='x', pady=10)

# Logo and App Name
logo_label = tk.Label(header_frame, image=logo, bg='#5D2E2E')
logo_label.pack(side='left', padx=10)

app_name = tk.Label(header_frame, text="Purse Pal", font=("Arial", 30, "bold"), bg='#5D2E2E', fg='white')
app_name.pack(side='left', padx=10)

# Right Side of Header
header_right_frame = tk.Frame(header_frame, bg='#5D2E2E')
header_right_frame.pack(side='right')

user_icon = tk.Label(header_right_frame, text="👤", font=("Arial", 25), bg='#5D2E2E', fg='white')
user_icon.pack(side='right', padx=5)

user_label = tk.Label(header_right_frame, text="Hello, User", font=("Arial", 20), bg='#5D2E2E', fg='white')
user_label.pack(side='right', padx=5)

# Balance and Reward Section
balance_frame = tk.Frame(root, bg='#845353')
balance_frame.pack(fill='x', pady=10, padx=20)

balance_label = tk.Label(balance_frame, text="NPR XXXX.XX\nBalance", font=("Arial", 20, "bold"), bg='#845353', fg='white')
balance_label.pack(side='left', padx=20, pady=20)

eye_icon = tk.Label(balance_frame, text="👁", font=("Arial", 30), bg='#845353', fg='white')
eye_icon.pack(side='left', padx=20)

reward_label = tk.Label(balance_frame, text="XXXX.XX\nReward points", font=("Arial", 20, "bold"), bg='#845353', fg='white')
reward_label.pack(side='left', padx=20)

gift_icon = tk.Label(balance_frame, text="🎁", font=("Arial", 30), bg='#845353', fg='white')
gift_icon.pack(side='left', padx=20)

# Action Buttons Section
action_frame = tk.Frame(root, bg='#5D2E2E')
action_frame.pack(fill='x', pady=10)

def redirect(): 
    root.destroy() 
    import sendmoney
        

button_texts = ["Send Money"]
for text in button_texts:
    btn = tk.Button(action_frame, text=text, font=("Arial", 15, "bold"), bg='#845353', fg='white', padx=20, pady=10, command=redirect)
    btn.pack(side='left', padx=20)

# Promotional Section
promo_frame = tk.Frame(root, bg='#5D2E2E')
promo_frame.pack(fill='x', pady=10, padx=20)

promo_image_path = './pic2.0.png'  # Replace with your image path
promo_image = Image.open(promo_image_path)
promo_image = promo_image.resize((250, 150), Image.LANCZOS)
promo_photo = ImageTk.PhotoImage(promo_image)

promo_label = tk.Label(promo_frame, image=promo_photo, bg='#5D2E2E')
promo_label.pack(side='left', padx=10)

promo_text = tk.Label(promo_frame, text="No Cash!\nNo Card!\nNo Worries\nWe got You 👍", font=("Arial", 20, "bold"), bg='#5D2E2E', fg='white', justify='left')
promo_text.pack(side='left', padx=20)

# Services Section
services_frame = tk.LabelFrame(root, text="*Our Services", font=("Arial", 20, "italic"), bg='#5D2E2E', fg='white', padx=20, pady=20)
services_frame.pack(fill='x', pady=20, padx=20)

def service_redirect(page):
    if (page == "Topup & Data"):
        import topup
    elif(page == "Airlines"): 
        import Flightfe
    elif (page == "Movies"): 
        import movies
    elif(page=="Bus Ticket"): 
        print(page)
        import busticket
    elif (page == "View Transactions"):
        print(page)
        import Afrontend
    else: 
        print("Error")
    root.destroy()
    
btn_list = []
btn_list.append(tk.Button(services_frame, text="Topup & Data", font=("Arial", 15), bg='#845353', fg='white', padx=10, pady=10, command=lambda:service_redirect("Topup & Data")))
btn_list.append(tk.Button(services_frame, text="Airlines", font=("Arial", 15), bg='#845353', fg='white', padx=10, pady=10, command=lambda:service_redirect("Airlines")))
btn_list.append(tk.Button(services_frame, text="Movies", font=("Arial", 15), bg='#845353', fg='white', padx=10, pady=10, command=lambda:service_redirect("Movies")))
btn_list.append(tk.Button(services_frame, text="Bus Ticket", font=("Arial", 15), bg='#845353', fg='white', padx=10, pady=10, command=lambda:service_redirect("Bus Ticket")))
btn_list.append(tk.Button(services_frame, text="View Transactions", font=("Arial", 15), bg='#845353', fg='white', padx=10, pady=10, command=lambda:service_redirect("View Transactions")))
    

    

btn_list[0].pack(side='left', padx=20, pady=10)
btn_list[1].pack(side='left', padx=20, pady=10)
btn_list[2].pack(side='left', padx=20, pady=10)
btn_list[3].pack(side='left', padx=20, pady=10)
btn_list[4].pack(side='left', padx=20, pady=10)


# More Section (On the right side)
more_frame = tk.LabelFrame(root, text="More....", font=("Arial", 15, "italic"), bg='#5D2E2E', fg='white', padx=20, pady=20)
more_frame.pack(side='right', pady=20, padx=20, fill='y')

more_options = ["View Statement", "Transaction Limit", "My Payments", "Support & Call", "About Us", "Settings"]
for option in more_options:
    lbl = tk.Label(more_frame, text=f". {option}", font=("Arial", 15), bg='#5D2E2E', fg='lightblue', anchor='w')
    lbl.pack(anchor='w', pady=10)

# Run the main loop
root.mainloop()