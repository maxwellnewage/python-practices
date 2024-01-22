"""
Flashy App
"""

from tkinter import Tk, Canvas, PhotoImage, Button
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    data_to_learn = pd.DataFrame(to_learn)
    data_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


if __name__ == '__main__':
    window = Tk()
    window.title("Flashy")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    flip_timer = window.after(3000, func=flip_card)

    canvas = Canvas(width=800, height=526)
    card_front_img = PhotoImage(file="images/card_front.png")
    card_back_img = PhotoImage(file="images/card_back.png")
    card_background = canvas.create_image(400, 263, image=card_front_img)
    card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
    card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=2)

    cross_image = PhotoImage(file="images/wrong.png")
    unknown_btn = Button(image=cross_image, highlightthickness=0, command=next_card)
    unknown_btn.grid(row=1, column=0)

    check_image = PhotoImage(file="images/right.png")
    known_btn = Button(image=check_image, highlightthickness=0, command=is_known)
    known_btn.grid(row=1, column=1)

    next_card()

    window.mainloop()
