from tkinter import *
import random

C_score=0
P_score=0

choice=["rock","paper","siccors"]

def play(pl_choice):
    global C_score, P_score
    cp_choice=random.choice(choice)
    computer_choice.config(text=f"computer selected: {cp_choice}")
    if pl_choice == cp_choice:
        subtitle.config(text="Its a...Tie!",fg="grey")
    elif pl_choice == "rock" and cp_choice == "siccors":
        subtitle.config(text="Its a...WIN!",fg="goldenrod")
        P_score+=1
        player_score.config(text=f"Player Score: {P_score}")
    elif pl_choice == "paper" and cp_choice == "rock":
        subtitle.config(text="Its a...WIN!",fg="goldenrod")
        P_score+=1
        player_score.config(text=f"Player Score: {P_score}")
    elif pl_choice == "siccors" and cp_choice == "paper":
        subtitle.config(text="Its a...WIN!",fg="goldenrod")
        P_score+=1
        player_score.config(text=f"Player Score: {P_score}")
    else:
        subtitle.config(text="Its a...Loser womp womp :(",fg="red")
        C_score+=1
        computer_score.config(text=f"Computer Score: {C_score}")


def rockcliked():
    player_choice.config(text="You Selected Rock")
    play("rock")

def papercliked():
    player_choice.config(text="You Selected Paper")
    play("paper")

def scissorscliked():
    player_choice.config(text="You Selected Sciccors")
    play("siccors")

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

rock = Button(window, text="Rock", width=10, height=2, bg="pink", command=rockcliked)
rock.grid(row=2, column=2, padx=10)

paper = Button(window, text="Paper", width=10, height=2, bg="lightgrey", command=papercliked)
paper.grid(row=2, column=3, padx=10)

scissors = Button(window, text="Scissors", width=10, height=2, bg="lightblue", command=scissorscliked)
scissors.grid(row=2, column=4, padx=10)

score_label = Label(window, text="Score", font=("Helvetica", 12),fg="black",bg="white")
score_label.grid(row=3, column=1, pady=30)

player_choice = Label(window, text="You Selected:", font=("Helvetica", 12),fg="black",bg="white")
player_choice.grid(row=3, column=2)

computer_choice = Label(window, text="Computer Selected:", font=("Helvetica", 12),fg="black",bg="white")
computer_choice.grid(row=4, column=2)

player_score = Label(window, text="Player Score: 0", font=("Helvetica", 12),fg="black",bg="white")
player_score.grid(row=3, column=3, padx=20)

computer_score = Label(window, text="Computer Score: 0", font=("Helvetica", 12),fg="black",bg="white")
computer_score.grid(row=4, column=3, padx=20)

window.mainloop()
