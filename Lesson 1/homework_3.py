from tkinter import *
import random

def check_awn():
    user = int(guess_entry.get())
    if user == rando:
        high_low.config(text="Correct!")
    elif user < rando:
        high_low.config(text="Too low!")
    elif user > rando:
        high_low.config(text="Too high!")



rando=random.randint(1,50)

window = Tk()
window.title("Product Guessing Game")
window.geometry("400x200")
window.configure(bg="white")


heading = Label(window, text="Product Guessing Game", font=("Helvetica", 18, "bold"), bg="white")
heading.place(x=10,y=10)

tries_label = Label(window, text="You have 5 tries left", font=("Helvetica", 12), bg="white")
tries_label.place(x=10,y=40)

#guess_frame = Frame(window, bg="white",)
#guess_frame.place(x=10,y=80)

guess_label = Label(window, text="Your Guess:", font=("Helvetica", 12), bg="white")
guess_label.place(x=10,y=103)

guess_entry = Entry(window, width=25)
guess_entry.place(x=80,y=100)

check_button = Button(window, text="Check", bg="red", fg="red", font=("Helvetica", 10, "bold"),command=check_awn)
check_button.place(x=330,y=103)

high_low = Label(window, text="", font=("Helvetica", 12), bg="light gray",fg="black")
high_low.place(x=205,y=153)

window.mainloop()

