from tkinter import*
from tkinter import ttk

window= Tk()
window.geometry("750x500")

item_entry_text= Label(window,text="Enter item:")
item_entry_text.pack(side=TOP)

item_entry=Entry(window,text="")
item_entry.pack(side=TOP)

frame=Frame(window)
frame.pack(side=TOP)

add_button=Button(frame,text="ADD",fg="Red",bg="White")
add_button.grid(row=2,column=2)

edit_button=Button(frame,text="EDIT",fg="Yellow",bg="White")
edit_button.grid(row=2,column=1,padx=150)

delete_button=Button(frame,text="DELETE",fg="black",bg="White")
delete_button.grid(row=3,column=2)

clearall_button=Button(frame,text="CLEAR ALL",fg="purple",bg="White")
clearall_button.grid(row=3,column=1)

listbox = Listbox(frame, width=50, height=15)
listbox.grid(columnspan=4)

window.mainloop()