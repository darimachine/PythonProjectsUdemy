from random import randint,choice
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars=[]
        self.counter=6
        self.speed_up=STARTING_MOVE_DISTANCE
    def create_car(self):

        if self.counter>5:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(choice(COLORS))
            random_y = randint(-250, 250)
            car.goto(300,random_y)
            self.all_cars.append(car)
            self.counter=0
        self.counter+=1

    def car_for(self):
        for car in self.all_cars:
            car.backward(self.speed_up)

    def car_speed(self):
        self.speed_up +=MOVE_INCREMENT






