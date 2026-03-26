import tkinter as tk
from operator import contains
from tkinter import ttk
from tkcalendar import DateEntry
from classes import Rental

root = tk.Tk()
root.title("Bike Rental system")
root.geometry("700x500") # Just an arbitrary size idk probably will change

errorMessage = tk.StringVar()

rentals = []

def submit():
    global errorMessage
    try:
        errorMessage.set("Incorrect value(s)")
        name = name_entry.get()
        rentalNo = int(rental_entry.get())
        bikeType = bike_type.get()
        amount = int(qty_entry.get().strip())
        hireDate = start_entry.get_date()
        returnDate = return_entry.get_date()

        if not name.replace(' ', '').isalpha():
            errorMessage.set("Name must only contain letters")
            raise ValueError("Name must only contain letters")
        if rentalNo < 0:
            errorMessage.set("Rental Number must be greater than 0")
            raise ValueError("Rental Number must be greater than 0")
        if 0 >= amount or amount > 50:
            errorMessage.set("Customer can only hire 1-50 bikes")
            raise ValueError("Customer can only hire 1-50 bikes")
        if returnDate < hireDate:
            errorMessage.set("Return date must be after hire date")
            raise ValueError("Return date must be after hire date")

        rentals.append(Rental(name, rentalNo, bikeType, amount, hireDate, returnDate))

        tree.insert("","end",values=rentals[len(rentals)-1].toTuple()) # Getting the index for selection is a bit weird but we cant add anything else between the first entry and running this so its all good (trust me bro)

        value_error.grid_forget()
    except ValueError as e:
        value_error.grid(row=6, column=2)

def removeSelected():
    selected = tree.selection()
    if not selected:
        return

    for item in selected:
        values = tree.item(item)["values"]

        for r in rentals:
            if r.toTuple() == tuple(values):
                rentals.remove(r)
                break # return would skip tree.delete() so i switched to break

        tree.delete(item)


form = tk.Frame(root)
form.pack(anchor="w", padx=20)

tk.Label(form, text="Customer Name").grid(row=0, column=0)
name_entry = tk.Entry(form)
name_entry.grid(row=0, column=1)

tk.Label(form, text="Rental Number").grid(row=1, column=0)
rental_entry = tk.Entry(form)
rental_entry.grid(row=1, column=1)

tk.Label(form, text="Bike Type").grid(row=2, column=0)
bike_type = ttk.Combobox(form, values=["Mountain", "Road", "Electric"], state="readonly")
bike_type.grid(row=2, column=1)

tk.Label(form, text="Quantity (1-50)").grid(row=3, column=0)
qty_entry = tk.Entry(form)
qty_entry.grid(row=3, column=1)

tk.Label(form, text="Start Date").grid(row=4, column=0)
start_entry = DateEntry(form, date_pattern="dd/MM/yyyy", state="readonly")
start_entry.grid(row=4, column=1)

tk.Label(form, text="Return Date").grid(row=5, column=0)
return_entry = DateEntry(form, date_pattern="dd/MM/yyyy", state="readonly")
return_entry.grid(row=5, column=1)

tk.Button(form, text="Submit", command=submit).grid(row=6, column=1, pady=10)
tk.Button(form, text="Remove Selected", command=removeSelected).grid(row=6, column=0)
value_error = tk.Label(form, textvariable=errorMessage, fg="red")

headings = ("Name", "Rental #", "Type", "Amount", "Start Date", "Return Date")

tree = ttk.Treeview(root, columns=headings, show="headings")

for col in headings:
    tree.heading(col, text=col)
    tree.column(col, width=110, stretch=True)
tree.pack(fill="both", expand=True)

root.mainloop()