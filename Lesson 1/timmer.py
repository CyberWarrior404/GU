from tkinter import *
from time import strftime

bg="black"
fg="white"

def update():
    global bg,fg
    t1me=strftime("%H:%M:%S %p")
    time_label.config(text=t1me,bg=bg,fg=fg)
    time_label.after(1000,update)
    bg,fg=fg,bg



window=Tk()

time_label= Label(window,bg="white", fg="black", font=("roboto",22,"bold"))
time_label.pack(side=TOP)

update()

window.mainloop()