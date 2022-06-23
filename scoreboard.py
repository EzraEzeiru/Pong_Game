from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80 , "normal")


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def add_l_paddle(self):
        self.clear()
        self.score += 1
        self.write(arg=f"{self.score}", align="center", font=FONT)

    def add_r_paddle(self):
        self.clear()
        self.score += 1
        self.write(arg=f"{self.score}", align="center", font=FONT)
