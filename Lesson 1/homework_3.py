from tkinter import *

window = Tk()
window.title("Product Guessing Game")
window.geometry("400x200")
window.configure(bg="white")


heading = Label(window, text="Product Guessing Game", font=("Helvetica", 18, "bold"), bg="white")
heading.pack(pady=10)

tries_label = Label(window, text="You have 5 tries left", font=("Helvetica", 12), bg="white")
tries_label.pack()

guess_frame = Frame(window, bg="white")
guess_frame.pack(pady=20)

guess_label = Label(guess_frame, text="Your Guess:", font=("Helvetica", 12), bg="white")
guess_label.pack(side=LEFT, padx=5)

guess_entry = Entry(guess_frame, width=25)
guess_entry.pack(side=LEFT, padx=5)

check_button = Button(guess_frame, text="Check", bg="red", fg="red", font=("Helvetica", 10, "bold"))
check_button.pack(side=LEFT, padx=5)


window.mainloop()
