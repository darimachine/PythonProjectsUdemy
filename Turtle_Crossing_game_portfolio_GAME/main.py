import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
car = CarManager()
screen.listen()
screen.title("My Turtle Game  :)")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.car_for()
    screen.onkeypress(player.up, "Up")
    if player.ycor()>280:
        player.end_of_level()
        score.level_up()
        car.car_speed()


    for cars in car.all_cars:
        if cars.distance(player) < 19:
            score.game_over()
            score.high()
            game_is_on=False







screen.exitonclick()
