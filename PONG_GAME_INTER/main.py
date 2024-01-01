from turtle import Turtle,Screen
from paddle import Padle
from line import Line
from ball import Ball
from scoreboard import Score
import time
screen = Screen()
screen.setup(1000,600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

line = Line()
ball = Ball()
score = Score()
r_paddle = Padle((470,0))
l_paddle = Padle((-475,0))

screen.listen()
game_on = True
indicator_y =-1
indicator_x = 1
while game_on:

    time.sleep(0.02)
    screen.update()
    screen.onkeypress(r_paddle.go_up, "Up")
    screen.onkeypress(r_paddle.go_down, "Down")
    screen.onkeypress(l_paddle.go_up, "w")
    screen.onkeypress(l_paddle.go_down, "s")
    ball.move(indicator_x,indicator_y)
    if ball.ycor()>280 or ball.ycor()<-280:
        indicator_y *= -1
    if ball.xcor()>445 and ball.distance(r_paddle)<50 or ball.xcor()<-445 and ball.distance(l_paddle)<50:
        indicator_x *= -1
    #score for the right side
    if ball.xcor()>490:
        score.r_side_score()
        indicator_x *= -1
        indicator_y *= -1
        ball.home()

    # score for the left side
    elif ball.xcor()<-490:

        score.l_side_score()
        indicator_x *= -1
        indicator_y *= -1
        ball.home()







screen.exitonclick()