from tkinter import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
import random

try:
    df = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("french_words.csv")
dic_words= df.to_dict(orient="records")
word = {}

def rand_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    #grab a random word from dictionary and changing the canvas text with the new word
    word = random.choice(dic_words)
    canvas.itemconfig(text1, text="French", fill="black")
    canvas.itemconfig(text2, text=word['French'],fill="black")
    canvas.itemconfig(front_card, image=card_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(text1 ,text="English",fill="white")
    canvas.itemconfig(text2, text=word["English"],fill="white")
    canvas.itemconfig(front_card, image=back_img)

def is_known():
    dic_words.remove(word)
    rand_word()
    data = pd.DataFrame(dic_words)
    data.to_csv("words_to_learn.csv",index=False)

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)
card_img = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")

front_card = canvas.create_image(400,263,image=card_img)

text1 = canvas.create_text(400,150,text="French", font=("Ariel",40,"italic"))
text2 = canvas.create_text(400,263,text="", font=("Ariel",60,"bold"))


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)

right_img = PhotoImage(file="right.png")
wrong_img = PhotoImage(file="wrong.png")

button1 = Button(image=right_img,highlightthickness=0,command=is_known)
button1.grid(column=0,row=1)

button2 = Button(image=wrong_img,highlightthickness=0,command=rand_word)
button2.grid(column=1,row=1)

rand_word()

window.mainloop()
