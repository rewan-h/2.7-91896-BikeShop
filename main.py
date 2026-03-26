import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from classes import Rental

MAX_HIRE_AMOUNT = 50
WIN_WIDTH = 700
WIN_HEIGHT = 500

root = tk.Tk()
root.title("Bike Rental system")
root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")

errorMessage = tk.StringVar()

rentals = []

def submit(): # Function called when submit button is clicked for adding customer data
    global errorMessage
    try:
        errorMessage.set("Incorrect value(s)") # Default to this error message if there is some unaccounted for error (typically in the int() cast)

        # Place all relevant values into more readable variables for input handling and processing
        name = name_entry.get()
        rentalNo = int(rental_entry.get())
        bikeType = bike_type.get()
        amount = int(qty_entry.get().strip())
        hireDate = start_entry.get_date()
        returnDate = return_entry.get_date()

        # Input Handling
        if not name.replace(' ', '').isalpha(): # Remove spaces for the isalpha() check as they aren't alphabetical characters
            errorMessage.set("Name must only contain letters")
            raise ValueError("Name must only contain letters")
        if rentalNo < 0:
            errorMessage.set("Rental Number must be greater than 0")
            raise ValueError("Rental Number must be greater than 0")
        if 0 >= amount or amount > MAX_HIRE_AMOUNT:
            errorMessage.set(f"Customer can only hire 1-{MAX_HIRE_AMOUNT} bikes")
            raise ValueError(f"Customer can only hire 1-{MAX_HIRE_AMOUNT} bikes")
        if returnDate < hireDate:
            errorMessage.set("Return date must be after hire date")
            raise ValueError("Return date must be after hire date")

        rentals.append(Rental(name, rentalNo, bikeType, amount, hireDate, returnDate))

        tree.insert("","end",values=rentals[len(rentals)-1].toTuple()) # Getting the index for selection is a bit weird but we cant add anything else between the first entry and running this so its all good (trust me bro)

        value_error.grid_forget() # No error, we can hide any present error message
    except ValueError as e: # If an error is thrown we just add the error message label back to the grid to display it
        value_error.grid(row=6, column=2)

def removeSelected():
    selected = tree.selection()
    if not selected: # No item in the tree is selected
        return

    for item in selected: # It is possible to select multiple items on the tree se we must account for all of them
        values = tree.item(item)["values"] # Gets the "value" part of the tree dictionary (contains our set values)

        for r in rentals:
            if r.toTuple() == tuple(values): # Recursively checks if the selected values matches the r'th tuple in rentals
                rentals.remove(r)
                break # return would skip tree.delete() so i switched to break

        tree.delete(item)



#TODO: Need to comment and cleanup this part of the app
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

tk.Label(form, text=f"Quantity (1-{MAX_HIRE_AMOUNT})").grid(row=3, column=0)
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