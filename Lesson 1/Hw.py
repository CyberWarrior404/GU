from tkinter import *
from tkinter import ttk

def add():
    name=name_entry.get()
    address=address_entry.get()
    mobile=mobile_entry.get()
    email=email_entry.get()
    birthday=birthday_entry.get()
    name_entry.delete(0,END)
    address_entry.delete(0,END)
    mobile_entry.delete(0,END)
    email_entry.delete(0,END)
    birthday_entry.delete(0,END)
    listbox.insert(END,name)

window = Tk()
window.title("Address Book")
window.geometry("750x400")

title = Label(window, text="My Address Book", font=("Arial", 14, "bold"))
title.grid(row=0, column=0, padx=10, pady=5, sticky="w")


open_btn = Button(window, text="Open", width=10)
open_btn.grid(row=0, column=1, padx=10, pady=5,)


listbox = Listbox(window, width=35, height=15)
listbox.grid(row=1, column=0, rowspan=6, padx=10, pady=5)


Label(window, text="Name:").grid(row=1, column=1, padx=5, pady=5)
name_entry = Entry(window, width=30)
name_entry.grid(row=1, column=2, padx=5, pady=5)

Label(window, text="Address :").grid(row=2, column=1, padx=5, pady=5)
address_entry = Entry(window, width=30)
address_entry.grid(row=2, column=2, padx=5, pady=5)

Label(window, text="Mobile:").grid(row=3, column=1, padx=5, pady=5)
mobile_entry = Entry(window, width=30)
mobile_entry.grid(row=3, column=2, padx=5, pady=5)

Label(window, text="Email:").grid(row=4, column=1, padx=5, pady=5)
email_entry = Entry(window, width=30)
email_entry.grid(row=4, column=2, padx=5, pady=5)

Label(window, text="Birthday:").grid(row=5, column=1, padx=5, pady=5)
birthday_entry = Entry(window, width=30)
birthday_entry.grid(row=5, column=2, padx=5, pady=5)

edit_btn = Button(window, text="Edit", width=10)
edit_btn.grid(row=7, column=0, padx=10, pady=5)

delete_btn = Button(window, text="Delete", width=10)
delete_btn.grid(row=7, column=0,padx=10, pady=5)

update_btn = Button(window, text="Update/Add", width=12,command=add)
update_btn.grid(row=7, column=2, padx=10, pady=5)

save_btn = Button(window, text="Save", width=50)
save_btn.grid(row=8, column=0, columnspan=3, pady=10)

window.mainloop()
