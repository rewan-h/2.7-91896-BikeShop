import tkinter as tk
from classes import Rental

root = tk.Tk()
root.title("Bike Rental system")
root.geometry("700x500") # Just an arbitrary size idk probably will change

rental = Rental("Joe",1,"MTB",1,"Test","Test")
#Doesnt crash yipee

#TODO Literally the entire GUI

root.mainloop()