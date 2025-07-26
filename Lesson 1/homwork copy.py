from tkinter import *

window = Tk()

window.geometry("750x500")

heading = Label(window, text="Celcius --> Fahrenheit", font=("roboto", 40,"bold"))
heading.place(x=175,y=10)

celcius_label = Label(window, text="Enter temprature in celcius:", font=("roboto", 15,"bold"))
celcius_label.place(x=150,y=90)

celcius_entry = Entry(window, width=15)
celcius_entry.place(x=375,y=90)

calculate_button = Button(window, width=15, height=3, background="green", text="Calculate", fg="dark green")
calculate_button.place(x=250,y=120)
window.mainloop()
