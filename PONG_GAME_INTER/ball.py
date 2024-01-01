from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
    def move(self,x,y):
            new_x = self.xcor()+(10*x)
            new_y=self.ycor()+(10 *y)
            self.goto(new_x,new_y)

