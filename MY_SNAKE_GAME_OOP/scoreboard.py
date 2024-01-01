from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Couriel", 20, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        with open("data.txt",mode="r") as file:
            self.high_score = file.read()
        self.hideturtle()
        self.score = 0
        self.shapesize(2)
        self.goto(0, 260)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    def score_calc(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score >int(self.high_score):
            self.high_score=self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score=0
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
       

    # def game_over(self):
    #     self.home()
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)