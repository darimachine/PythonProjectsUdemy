# def mouse_click(x,y):
#     print(x,y)
# turtle.onscreenclick(mouse_click)
# turtle.mainloop()
import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
title = "Guess The State"
repeat = []
country = turtle.Turtle()
country.hideturtle()
country.penup()
country.speed(0)
country.color("black")
all_states = data["state"].to_list()

while len(repeat) < 50:
    answer = screen.textinput(title, "What's another state's name").title()
    if answer == "Exit":
        missing_state = [state for state in all_states if state not in repeat]
        all_states = {
            "Not Guessed": missing_state
        }
        not_guessed = pd.DataFrame(all_states)
        not_guessed.to_csv("states_to_learn.csv")
        break

    if answer in all_states:
        if answer not in repeat:
            a = data[data.state == answer]
            country.goto(int(a.x), int(a.y))
            country.write(a.state.item(), align="center", font=("Arial", 6, "bold"))
            repeat.append(answer)
            title = f"{len(repeat)}/50 States Correct"

screen.exitonclick()
