from turtle import Turtle

FONT = ('Courier', 14, 'normal')
GAME_OVER_FONT = ('Courier', 20, 'normal')
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score + 1} High Score: {self.high_score}", False, ALIGNMENT, font=FONT)
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = -1
        self.update_score()
