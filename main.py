import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from classes import Rental

root = tk.Tk()
root.title("Bike Rental system")
root.geometry("700x500") # Just an arbitrary size idk probably will change

rentals = []

def submit():
    try:
        rentals.append(Rental(name_entry.get(), rental_entry.get(), bike_type.get(), qty_entry.get(), start_entry.get_date(), return_entry.get_date()))

        tree.insert("","end",values=rentals[len(rentals)-1].toTuple()) # Getting the index for selection is a bit weird but we cant add anything else between the first entry and running this so its all good (trust me bro)

        value_error.grid_forget()
    except ValueError as e:
        value_error.grid(row=6, column=0)
        print(e)

def removeSelected():
    return

form = tk.Frame(root)
form.pack()

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

tk.Label(form, text="Return Date").grid(row=5, column=0 )
return_entry = DateEntry(form, date_pattern="dd/MM/yyyy", state="readonly")
return_entry.grid(row=5, column=1)

tk.Button(form, text="Submit", command=submit).grid(row=6, column=1, pady=10)
#tk.Button(form, text="Remove Selected", command=removeSelected)
#TODO: The above comment needs to be implemented
value_error = tk.Label(form, text="Incorrect value(s)", fg="red")

headings = ("Name", "Rental #", "Type", "Amount", "Start Date", "Return Date")

tree = ttk.Treeview(root, columns=headings, show="headings")

for col in headings:
    tree.heading(col, text=col)
    tree.column(col, width=110, stretch=True)
tree.pack(fill="both", expand=True)

root.mainloop()