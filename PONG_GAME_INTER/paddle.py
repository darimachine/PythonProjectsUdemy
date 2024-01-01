from turtle import Turtle
class Padle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle()
    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(self.position)
    def go_up(self):
        if self.ycor()<250:
            new_y = self.ycor()+20
            self.goto(self.position[0],new_y)
    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.position[0], new_y)



