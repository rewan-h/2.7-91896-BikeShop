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
        value_error.grid_forget()
    except ValueError as e:
        value_error.grid(row=6, column=0)
        print(e)

#TODO About half of the entire GUI (The list with customer info etc)
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
start_entry = DateEntry(form, date_pattern="dd/MM/yyyy")
start_entry.grid(row=4, column=1)

tk.Label(form, text="Return Date").grid(row=5, column=0 )
return_entry = DateEntry(form, date_pattern="dd/MM/yyyy")
return_entry.grid(row=5, column=1)

tk.Button(form, text="Submit", command=submit).grid(row=6, column=1, pady=10)
value_error = tk.Label(form, text="Incorrect value(s)", fg="red")


root.mainloop()