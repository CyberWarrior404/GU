from tkinter import *
from tkinter import filedialog, messagebox

window = Tk()
window.title("Item Manager")
window.geometry("500x400")
window.configure(bg="white")

label = Label(window, text="Enter Item:", font=("Helvetica", 12), bg="white")
label.pack(pady=(10,0))

entry = Entry(window, width=40, font=("Helvetica", 12))
entry.pack(pady=5)

button_frame = Frame(window, bg="white")
button_frame.pack(pady=10)

add_button = Button(window, text="ADD", bg="green", fg="white", width=10)
add_button.grid(row=0, column=0, padx=5, pady=5)

edit_button = Button(window, text="EDIT", bg="orange", fg="black", width=10)
edit_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = Button(window, text="DELETE", bg="red", fg="white", width=10)
delete_button.grid(row=1, column=0, padx=5, pady=5)

clear_button = Button(window, text="CLEAR ALL", bg="purple", fg="white", width=10)
clear_button.grid(row=1, column=1, padx=5, pady=5)

listbox = Listbox(window, width=60, height=10, font=("Helvetica", 12))
listbox.pack(pady=10)

file_frame = Frame(window, bg="white")
file_frame.pack(pady=10)

open_button = Button(window, text="OPEN FILE", bg="dodgerblue", fg="white", width=15, command=open_file)
open_button.grid(row=0, column=0, padx=10)

save_button = Button(window, text="SAVE FILE", bg="gray", fg="white", width=15, command=save_file)
save_button.grid(row=0, column=1, padx=10)


window.mainloop()
