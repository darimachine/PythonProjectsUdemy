from random import randint
from turtle import Turtle, Screen

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
width = 500
screen.setup(width=width, height=400)
space = -120
user_bet = screen.textinput('Make your bet', 'Which turtle will win the race, Enter a color')
all_turtles = []
for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-1 * (width / 2 - 15), (space))
    space += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:

    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on = False
            if t.fillcolor() == user_bet:
                print(f"You have won! The {t.fillcolor()} turtle is the winner")
            else:
                print(f"You have lost! The {t.fillcolor()} turtle is the winner")

        distance = randint(0, 10)
        t.forward(distance)

screen.exitonclick()
