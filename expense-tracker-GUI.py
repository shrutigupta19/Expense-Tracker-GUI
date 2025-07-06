import tkinter as tk
from tkinter import messagebox


budget_data = []


def add_transaction():
    date = entry_date.get()
    category = entry_category.get()
    amount = entry_amount.get()
    description = entry_description.get()

    
    if date == "" or category == "" or amount == "":
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    
    budget_data.append({"Date": date, "Category": category, "Amount": amount, "Description": description})

    
    entry_date.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_description.delete(0, tk.END)

    messagebox.showinfo("Success", "Transaction added successfully.")


def show_budget():
    
    listbox.delete(0, tk.END)

    for transaction in budget_data:
        transaction_str = f"{transaction['Date']} | {transaction['Category']} | {transaction['Amount']} | {transaction['Description']}"
        listbox.insert(tk.END, transaction_str)


window = tk.Tk()
window.title("Budget Tracker")


label_date = tk.Label(window, text="Date:")
label_date.grid(row=0, column=0, sticky="E")
entry_date = tk.Entry(window)
entry_date.grid(row=0, column=1)

label_category = tk.Label(window, text="Category:")
label_category.grid(row=1, column=0, sticky="E")
entry_category = tk.Entry(window)
entry_category.grid(row=1, column=1)

label_amount = tk.Label(window, text="Amount:")
label_amount.grid(row=2, column=0, sticky="E")
entry_amount = tk.Entry(window)
entry_amount.grid(row=2, column=1)

label_description = tk.Label(window, text="Description:")
label_description.grid(row=3, column=0, sticky="E")
entry_description = tk.Entry(window)
entry_description.grid(row=3, column=1)

button_add = tk.Button(window, text="Add Transaction", command=add_transaction)
button_add.grid(row=4, column=0, columnspan=2, pady=10)

listbox = tk.Listbox(window, width=50)
listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

button_show = tk.Button(window, text="Show Budget", command=show_budget)
button_show.grid(row=6, column=0, columnspan=2, pady=10)


window.mainloop()
