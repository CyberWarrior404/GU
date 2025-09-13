from tkinter import*
from tkinter.ttk import Combobox

def printTable(droplist):
    try:
        gen = int(droplist.get())  # Convert the selected value to an integer
        for i in range(1, 11):
            result = gen * i
            all_results += f"{gen} * {i} = {result}/n"
            r3sult.config(text=all_results)
            print(f"{gen} * {i} = {result}")
    except ValueError:
        print("Please select a valid number from the dropdown list.")


window= Tk()
window.geometry("500x700")

heading=Label(window,text="Multiplication Table Bot",font=("Arial",25,"bold"))
heading.pack(side="top")

frame=Frame(window)
frame.pack(side="top")

placeholder=Label(frame,text="Choose a number")
placeholder.grid(row=0,column=0)

genrate=Button(frame,text="Generate",command=lambda: printTable(droplist))
genrate.grid(row=1,column=1)

droplist=Combobox(frame, values=[1,2,3,4,5,6,7,8,9,10])
droplist.grid(row=0,column=1)

r3sult=Label(frame,text="",fg="grey1",bg="grey")
r3sult.grid(row=3,column=1)

window.mainloop()
