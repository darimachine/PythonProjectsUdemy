from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

user_input = screen.textinput("Enter your Choice","Do you want to play the game with wall or without wall. Type 'y' for wall and 'n' without wall").lower()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if (snake.head.distance(food)) < 17:
        food.refresh()
        score.score_calc()
        snake.extend()
    if user_input =="n":
        if (snake.head.xcor()) > 295:
            snake.head.goto(-snake.head.xcor(), snake.head.ycor())
        elif (snake.head.xcor()) < -295:
            snake.head.goto(-snake.head.xcor(), snake.head.ycor())
        elif (snake.head.ycor()) > 295:
            snake.head.goto(snake.head.xcor(), -snake.head.ycor())
        elif (snake.head.ycor()) < -295:
            snake.head.goto(snake.head.xcor(), -snake.head.ycor())
    elif user_input=="y":
        if (snake.head.xcor())>295 or (snake.head.xcor()) < -295 or (snake.head.ycor()) > 295 or (snake.head.ycor()) < -295:
            snake.reset()
            score.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            snake.reset()
            score.reset()
screen.exitonclick()
