import tkinter as tk
from tkinter import messagebox

bids = []

def add_bid():
    name = name_entry.get().strip()
    try:
        amount = int(amount_entry.get().strip())
    except ValueError:
        messagebox.showerror("Invalid Input", "Amount must be a number.")
        return
    
    if not name:
        messagebox.showerror("Invalid Input", "Name cannot be empty.")
        return

    bids.append({"name": name, "amount": amount})
    bid_listbox.insert(tk.END, f"{name} - ₹{amount}")
    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def get_second_highest_bid():
    if not bids or len(bids) < 2:
        messagebox.showinfo("Result", "Not enough bidders.")
        return

    unique_bids = list(set(bid["amount"] for bid in bids))
    unique_bids.sort()

    if len(unique_bids) < 2:
        result = "All bidders placed the same bid."
    else:
        result = f"Second highest bid: ₹{unique_bids[-2]}"
    
    messagebox.showinfo("Result", result)

# GUI Setup
root = tk.Tk()
root.title("Second Highest Bid Finder")
root.geometry("400x400")
root.configure(bg="#f4f4f4")

tk.Label(root, text="Bidder Name:", bg="#f4f4f4").pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Bid Amount (₹):", bg="#f4f4f4").pack(pady=5)
amount_entry = tk.Entry(root, width=30)
amount_entry.pack()

tk.Button(root, text="Add Bid", command=add_bid, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(root, text="Find Second Highest", command=get_second_highest_bid, bg="#2196F3", fg="white").pack(pady=5)

tk.Label(root, text="Bids List:", bg="#f4f4f4").pack(pady=10)
bid_listbox = tk.Listbox(root, width=40, height=8)
bid_listbox.pack()

root.mainloop()
