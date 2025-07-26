from tkinter import *

window = Tk()

window.geometry("500x500")

heading = Label(window, text="DISTANCE CALCULATOR", font=("roboto", 20))
heading.place(x=150,y=10)

speed_label = Label(window, text="Speed", font=("roboto", 15,"bold"))
speed_label.place(x=75,y=40)

speed_entry = Entry(window, width=10)
speed_entry.place(x=75,y=65)

time_label = Label(window, text="Time", font=("roboto", 15,"bold"))
time_label.place(x=225,y=40)

time_entry = Entry(window, width=10)
time_entry.place(x=225,y=65)

distance_label = Label(window, text="Distance", font=("roboto", 15,"bold"))
distance_label.place(x=375,y=40)

distance_frame = Frame(window, width=100, height=25, background="white")
distance_frame.place(x=375,y=65)

calculate_button = Button(window, width=15, height=3, background="green", text="Calculate", fg="dark green")
calculate_button.place(x=185,y=90)
window.mainloop()