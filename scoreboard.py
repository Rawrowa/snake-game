from turtle import Turtle

# Font is custom
UI_FONT = ("pixelated", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.upd_score()

    def add_point(self):
        self.score += 1
        self.upd_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=UI_FONT)

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.upd_score()

    def upd_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}        HIGH SCORE: {self.high_score}", align="center", font=UI_FONT)
