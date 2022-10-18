from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 22, 'normal')



class Scoore(Turtle):
    def __init__(self):
        super(Scoore, self).__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score_calc = 0

        self.refrash_score()

    def game_ower(self):
        self.goto(0, 0)
        self.write(f"GAME OWER", True, align=ALIGN, font=FONT)


    def refrash_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score {self.score_calc}", True, align=ALIGN ,font=FONT)
        self.score_calc += 1