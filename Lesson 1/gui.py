from tkinter import *
from tkinter import ttk
screen = Tk()
screen.geometry("500x500")
style=ttk.Style()
style.theme_use("clam")
style.configure("TButton",background="red",foreground="white")
red_button= ttk.Button(screen, text="PRESS ME", style="TButton")
red_button.pack()

screen.mainloop()