from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

timer = None


def flip(card):
    # Change canvas background
    canvas.itemconfig(canvas_image, image=canvas_bg_back)
    # Change French to English
    canvas.itemconfig(language_text, text="English", fill="white")
    # Change French translation to English Translation
    canvas.itemconfig(word_text, text=card["English"], fill="white")
    window.after_cancel(timer)


def next_card():
    global timer
    if timer:
        window.after_cancel(timer)
    current_card = random.choice(data)
    canvas.itemconfig(canvas_image, image=canvas_bg_front)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    timer = window.after(3000, flip, current_card)


french_data = pandas.read_csv("data/french_words.csv")
data = french_data.to_dict(orient="records")

window = Tk()
window.title("Flash Cards")
window.config(width=1200, height=1200, padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas_bg_front = PhotoImage(file="images/card_front.png")
canvas_bg_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 275, image=canvas_bg_front)
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)

language_text = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 35, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 35, "bold"))

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, padx=50, pady=20, highlightbackground=BACKGROUND_COLOR,
                      command=next_card)
right_button.grid(column=0, row=3)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, padx=50, pady=20,
                      highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=1, row=3)

next_card()

window.mainloop()
