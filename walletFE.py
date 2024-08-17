import tkinter as tk
from tkinter import ttk

class PursePalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Purse Pal")
        self.configure(bg="#4c2c2c")
        self.geometry("900x700")
        self.create_widgets()

    def create_widgets(self):
        header_frame = tk.Frame(self, bg="#5b3a3a", pady=20, padx=20)
        header_frame.pack(fill=tk.X, pady=10, padx=10)

        balance_frame = tk.Frame(header_frame, bg="#5b3a3a")
        balance_frame.pack(side=tk.LEFT, padx=10)
        tk.Label(balance_frame, text="NPR XXXX.XX", bg="#5b3a3a", fg="white").pack()
        tk.Label(balance_frame, text="Balance", bg="#5b3a3a", fg="white").pack()

        reward_frame = tk.Frame(header_frame, bg="#5b3a3a")
        reward_frame.pack(side=tk.LEFT, padx=10)
        tk.Label(reward_frame, text="XXXX.XX", bg="#5b3a3a", fg="white").pack()
        tk.Label(reward_frame, text="Reward points", bg="#5b3a3a", fg="white").pack()

        actions_frame = tk.Frame(header_frame, bg="#5b3a3a")
        actions_frame.pack(side=tk.LEFT, padx=10)
        tk.Button(actions_frame, text="Send Money", bg="#5b3a3a", fg="white").pack(fill=tk.X)
        tk.Button(actions_frame, text="Add Money", bg="#5b3a3a", fg="white").pack(fill=tk.X)
        tk.Button(actions_frame, text="Banking Service", bg="#5b3a3a", fg="white").pack(fill=tk.X)
        tk.Button(actions_frame, text="Remittance", bg="#5b3a3a", fg="white").pack(fill=tk.X)
        tk.Button(actions_frame, text="Show QR", bg="#5b3a3a", fg="white").pack(fill=tk.X)

        banner_frame = tk.Frame(header_frame, bg="#5b3a3a")
        banner_frame.pack(side=tk.RIGHT, padx=10)
        banner_image = tk.PhotoImage(file="wallet.png")  # Adjust the path to the image accordingly
        tk.Label(banner_frame, image=banner_image, bg="#5b3a3a").pack()
        tk.Label(banner_frame, text="No Cash! No Card! No Worries\nWe got You", bg="#5b3a3a", fg="white").pack()
        tk.Label(banner_frame, text="Connect Your Bank with Purse Pal", bg="#5b3a3a", fg="white").pack()
        tk.Label(banner_frame, text="LINK NOW", bg="#5b3a3a", fg="blue").pack()

        services_frame = tk.Frame(self, bg="#5b3a3a", pady=20, padx=20)
        services_frame.pack(fill=tk.X, pady=10, padx=10)

        tk.Label(services_frame, text="*Our Services", bg="#5b3a3a", fg="white").pack(anchor="w")

        service_names = ["Topup & Data", "Water & Electricity", "Internet & TV", "Airlines",
                         "Movies", "Bus Ticket", "Hotel Booking", "Education Fee", "Insurance", "Others"]

        for i, service in enumerate(service_names):
            tk.Button(services_frame, text=service, bg="#5b3a3a", fg="white", width=15).grid(row=i//5, column=i%5, padx=10, pady=5)

        more_frame = tk.Frame(self, bg="#5b3a3a", pady=20, padx=20)
        more_frame.pack(side=tk.RIGHT, fill=tk.Y, pady=10, padx=10)

        tk.Label(more_frame, text="More....", bg="#5b3a3a", fg="white").pack(anchor="w")

        more_options = ["View Statement", "Transaction Limit", "My Payments", "Support & Call", "About Us", "Settings"]

        for option in more_options:
            tk.Label(more_frame, text=option, bg="#5b3a3a", fg="blue").pack(anchor="w", pady=5)

if __name__ == "__main__":
    app = PursePalApp()
    app.mainloop()
