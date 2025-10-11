from tkinter import *
import random

words = ["python", "jumble", "random", "tkinter", "widget"]
current_word=random.choice(words)
def get_jumbled_word(word):
    word_list = list(word)
    word_label.config(text=random.shuffle(current_word))
    

def check_word():
    user_input = entry.get().lower()
    if user_input == current_word:
        result_label.config(text="Correct!", fg="lightgreen")
    else:
        result_label.config(text=f"Wrong! It was '{current_word}'", fg="red")

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

check_button = Button(window, text="Check", bg="pink", fg="blue", font=("Arial", 12, "bold"), command=check_word)
check_button.pack(pady=5)

reset_button = Button(window, text="Reset", bg="blue", fg="Pink", font=("Arial", 12, "bold"),command=get_jumbled_word)
reset_button.pack(pady=5)

result_label = Label(window, text="", font=("Arial", 14), bg="black")
result_label.pack(pady=10)


window.mainloop()
