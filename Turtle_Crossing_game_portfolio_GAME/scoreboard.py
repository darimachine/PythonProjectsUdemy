from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        with open("track_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.write(f"Level: {self.level}       High Level: {self.high_score}", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}       High Level: {self.high_score}", align="center", font=FONT)

    def high(self):
        if self.level > self.high_score:
            self.high_score = self.level
            with open("track_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.clear()
        self.level = 1
        self.goto(0, 250)
        self.write(f"Level: {self.level}       High Level: {self.high_score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
