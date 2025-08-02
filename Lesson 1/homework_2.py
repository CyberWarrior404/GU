from tkinter import *

window = Tk()

window.geometry("500x300")

def submit():
    name = name_entry.get()
    age = age_entry.get()
    print("Name:", name)
    print("Age:", age)

heading = Label(window, text="Form", font=("roboto", 20))
heading.place(x=200, y=10)

name_label = Label(window, text="NAME:", font=("roboto", 15, "bold"))
name_label.place(x=75, y=40)

name_entry = Entry(window, width=20, bg="green")
name_entry.place(x=75, y=70)

age_label = Label(window, text="Age:", font=("roboto", 15, "bold"))
age_label.place(x=75, y=100)

age_entry = Entry(window, width=20, bg="green")
age_entry.place(x=75, y=130)

submit_button = Button(window, width=20, height=2, bg="blue", text="SUBMIT", fg="black", command=submit)
submit_button.place(x=150, y=170)

window.mainloop()
