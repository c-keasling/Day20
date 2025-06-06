from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Amazon Ember', 18, 'bold')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt",mode="r") as hs_file:
            self.high_score = int(hs_file.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0,y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as hs_file:
                hs_file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def score_point(self):
        self.score += 1
        self.update_scoreboard()
