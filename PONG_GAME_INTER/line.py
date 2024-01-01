from turtle import Turtle
class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 290)
        self.right(90)
        self.pensize(4)
        for i in range(40):
            if i % 2 == 0:
                self.penup()
            else:
                self.pendown()
            self.forward(15)