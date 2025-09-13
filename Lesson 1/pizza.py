from tkinter import *
from tkinter.ttk import Combobox

def orda_pizza():
    quantity= qty_combo.get()
    s1ze= size.get()
    pizza = pizza_combo.get()
    result= f"voila here is ton pizza{quantity} {s1ze} {pizza}"
    r3sult.config(text=result)
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

order_btn = Button(window, text="Order", font=("Arial", 12, "bold"), bg="blue", fg="black", width=15,command=orda_pizza)
order_btn.pack(pady=20)

size=StringVar()
radio1=Radiobutton(frame,text="Small",value="Small",variable=size)
radio2=Radiobutton(frame,text="Medium",value="Medium",variable=size)
radio3=Radiobutton(frame,text="Large",value="Large",variable=size)
size.set("Medium")

radio1.grid(row=0,column=3)
radio2.grid(row=1,column=3)
radio3.grid(row=2,column=3)


r3sult = Label(window, text="", fg="white", font=("Arial", 12))
r3sult.pack(pady=10)

window.mainloop()
