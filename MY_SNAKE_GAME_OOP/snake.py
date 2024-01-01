from turtle import Turtle
MY_COORDINATES = [(0,0),(-20,0),(-40,0)]
UP = 90
RIGHT=0
LEFT=180
DOWN = 270
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in MY_COORDINATES:
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(i)
            self.segments.append(snake)

    def extend(self):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        position = self.segments[-1].position()
        snake.goto(position)
        self.segments.append(snake)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()

        self.create_snake()
        self.head = self.segments[0]
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            x = self.segments[i-1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x,y)
        self.head.forward(20)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

