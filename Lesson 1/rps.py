from tkinter import *

window = Tk()
window.geometry("800x400")
window.configure(bg="white")
window.title("Rock Paper Scissors")

title = Label(window, text="ROCK PAPER SCISSORS", font=("Helvetica", 20, "bold"), bg="white")
title.grid(row=0, column=0, columnspan=5, pady=20)

subtitle = Label(window, text="Let's Start the Game...", font=("Helvetica", 12), fg="green", bg="white")
subtitle.grid(row=1, column=0, columnspan=5, pady=5)

options = Label(window, text="Your Options", font=("Helvetica", 12), bg="white")
options.grid(row=2, column=1, pady=20)

rock = Button(window, text="Rock", width=10, height=2, bg="pink")
rock.grid(row=2, column=2, padx=10)

paper = Button(window, text="Paper", width=10, height=2, bg="lightgrey")
paper.grid(row=2, column=3, padx=10)

scissors = Button(window, text="Scissors", width=10, height=2, bg="lightblue")
scissors.grid(row=2, column=4, padx=10)

score_label = Label(window, text="Score", font=("Helvetica", 12), bg="white")
score_label.grid(row=3, column=1, pady=30)

player_choice = Label(window, text="You Selected:", font=("Helvetica", 12), bg="white")
player_choice.grid(row=3, column=2)

computer_choice = Label(window, text="Computer Selected:", font=("Helvetica", 12), bg="white")
computer_choice.grid(row=4, column=2)

player_score = Label(window, text="Player Score:-", font=("Helvetica", 12), bg="white")
player_score.grid(row=3, column=3, padx=20)

computer_score = Label(window, text="Computer Score:-", font=("Helvetica", 12), bg="white")
computer_score.grid(row=4, column=3, padx=20)

window.mainloop()
