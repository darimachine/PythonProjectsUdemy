from turtle import Turtle
MY_FONT = ("Couriel",40,"normal")
ALIGNMENT = "center"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.hideturtle()
        self.sety(220)
        self.write(f"{self.r_score}      {self.l_score}", font=MY_FONT, align=ALIGNMENT)
    def r_side_score(self):
        self.r_score+=1
        self.clear()
        self.write(f"{self.r_score}      {self.l_score}", font=MY_FONT, align=ALIGNMENT)
    def l_side_score(self):
        self.l_score += 1
        self.clear()
        self.write(f"{self.r_score}      {self.l_score}", font=MY_FONT, align=ALIGNMENT)
