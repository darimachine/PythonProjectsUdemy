from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
def random_word():
    global flip_timer,word

    window.after_cancel(flip_timer)
    canva.itemconfig(card_image, image=card_front)
    word = random.choice(data)
    canva.itemconfig(canva_title,text="English",fill="black")
    canva.itemconfig(canva_word,text=word["English"],fill="black")
    flip_timer = window.after(3000, flip_card)
def flip_card():
    canva.itemconfig(card_image,image=card_back)
    canva.itemconfig(canva_title, text="Bulgarian",fill="white")
    canva.itemconfig(canva_word, text=word["Bulgarian"],fill="white")
def is_known():
    data.remove(word)
    new_data = pd.DataFrame(data)
    new_data.to_csv("data/words_to_learn.csv",index=False)
    random_word()

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,pady=50,padx=50)
flip_timer = window.after(3000, flip_card)
#pd
try:
    data = pd.read_csv("data/words_to_learn.csv")
    data = data.to_dict(orient="records")
except FileNotFoundError:
    data = pd.read_csv("data/bg_to_en.csv")
    data = data.to_dict(orient="records")

# canva
canva = Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canva.create_image(400, 263, image=card_front)
canva_title = canva.create_text(400,150,font=("Arial",40,"italic"))
canva_word = canva.create_text(400,263,font=("Arial",60,"bold"))
canva.grid(row=0,column=0,columnspan=2)
#button
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
right_btn = Button(image=right,highlightthickness=0,command=is_known)
right_btn.grid(row=1,column=0)
print(right_btn=="button")
wrong_btn = Button(image=wrong,highlightthickness=0,command=random_word)
wrong_btn.grid(row=1,column=1)
print(wrong_btn)
random_word()




window.mainloop()



