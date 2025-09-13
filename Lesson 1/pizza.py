from tkinter import *
from tkinter.ttk import Combobox



window = Tk()
window.geometry("500x400")
window.title("Pizza Hut Order")

heading = Label(window, text="Welcome to Pizza Hut", font=("Arial", 20, "bold"))
heading.pack(side="top", pady=15)

frame = Frame(window)
frame.pack(side="top", pady=10)

pizza_label = Label(frame, text="Select Your Fav Pizza")
pizza_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

pizza_combo = Combobox(frame, values=["Veg Extravaganza", "Margherita", "Paneer Makhani", "Pepperoni", "Cheese Burst"])
pizza_combo.grid(row=0, column=1, padx=10, pady=5)

qty_label = Label(frame, text="Enter Quantity")
qty_label.grid(row=1, column=0, padx=10, pady=5)

qty_combo = Combobox(frame, values=[1,2,3,4,5,6,7,8,9,10])
qty_combo.grid(row=1, column=1, padx=10, pady=5)

order_btn = Button(window, text="Order", font=("Arial", 12, "bold"), bg="blue", fg="white", width=15)
order_btn.pack(pady=20)

r3sult = Label(window, text="", fg="black", font=("Arial", 12))
r3sult.pack(pady=10)

window.mainloop()
