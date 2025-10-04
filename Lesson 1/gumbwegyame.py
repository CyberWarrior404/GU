from tkinter import *
import random



window = Tk()
window.title("JUMBLED WORD GAME")
window.geometry("400x300")
window.config(bg="black")

heading = Label(window, text="JUMBLED WORD GAME", font=("Arial", 18, "bold"), bg="black", fg="white")
heading.pack(pady=10)

word_label = Label(window, text="", font=("Arial", 16), bg="black", fg="white")
word_label.pack(pady=10)

entry = Entry(window, font=("Arial", 14))
entry.pack(pady=10, ipadx=20, ipady=5)

check_button = Button(window, text="Check", bg="pink", fg="blue", font=("Arial", 12, "bold"))
check_button.pack(pady=5)

reset_button = Button(window, text="Reset", bg="blue", fg="Pink", font=("Arial", 12, "bold"))
reset_button.pack(pady=5)

result_label = Label(window, text="hi", font=("Arial", 14), bg="black")
result_label.pack(pady=10)

window.mainloop()
