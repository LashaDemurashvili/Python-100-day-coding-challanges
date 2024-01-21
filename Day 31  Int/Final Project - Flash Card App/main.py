from tkinter import *
import pandas
import random


# constants
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_cards():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_card_img)

    # refresh after 3 seconds
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")  # fill - for color change
    canvas.itemconfig(card_background, image=back_card_image)


def is_known():
    # if current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)  # index=False - for no index
    next_cards()


window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_card_img)
card_title = canvas.create_text(400, 150, text=f"", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 265, text="", font=("Ariel", 40, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image)
cross_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, command=next_cards)
cross_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image)
check_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

# call function for run as sun as program start
next_cards()

window.mainloop()
