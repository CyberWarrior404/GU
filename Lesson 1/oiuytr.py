from tkinter import *

window = Tk()
window.geometry("1000x750")
window.title("Item Manager")

def add():
    item=item_entry.get()
    listbox.insert(END,item)
    item_entry.delete(0,END)

def clear():
    listbox.delete(0,END)

def delete():
    S_item=listbox.curselection()
    listbox.delete(S_item)

def edit():
    edit=listbox.curselection()
    meti=listbox.get(edit)
    item_entry.delete(0,END)
    item_entry.insert(END,meti)
    listbox.delete(edit)

item_entry_text = Label(window, text="Enter Item:", font=("Arial", 12))
item_entry_text.pack(pady=5)

item_entry = Entry(window, width=40)
item_entry.pack(pady=5)

frame = Frame(window)
frame.pack(pady=10)

add_button = Button(frame, text="ADD", bg="green", fg="green", width=12, height=2,command=add)
add_button.grid(row=0, column=0, padx=10, pady=5)

edit_button = Button(frame, text="EDIT", bg="orange", fg="orange", width=12, height=2,command=edit)
edit_button.grid(row=0, column=1, padx=10, pady=5)

delete_button = Button(frame, text="DELETE", bg="red", fg="red", width=12, height=2,command=delete)
delete_button.grid(row=1, column=0, padx=10, pady=5)

clearall_button = Button(frame, text="CLEAR ALL", bg="purple", fg="purple", width=12, height=2,command=clear)
clearall_button.grid(row=1, column=1, padx=10, pady=5)

listbox = Listbox(window, width=80, height=15)
listbox.pack(pady=10)

bottom_frame = Frame(window, bg="lightgray")
bottom_frame.pack(pady=10)  

open_button = Button(bottom_frame, text="OPEN FILE", bg="deepskyblue", fg="deepskyblue", width=15, height=2)
open_button.grid(row=0, column=0, padx=10)

save_button = Button(bottom_frame, text="SAVE FILE", bg="slategray", fg="slategray", width=15, height=2)
save_button.grid(row=0, column=1, padx=10)

window.mainloop()
