from tkinter import *

window = Tk()

window.geometry("500x500")

heading = Label(window, text="DISTANCE CALCULATOR", font=("roboto", 20))
heading.place(x=150,y=10)

speed_label = Label(window, text="Speed Kh/ms", font=("roboto", 15,"bold"))
speed_label.place(x=75,y=40)

speed_entry = Entry(window, width=10)
speed_entry.place(x=75,y=65)

time_label = Label(window, text="Time sec/min", font=("roboto", 15,"bold"))
time_label.place(x=225,y=40)

time_entry = Entry(window, width=10)
time_entry.place(x=225,y=65)
window.mainloop()