from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.lives = 3
        self.update_text()

    def update_text(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.sety(255)
        self.write(arg=f"Level {self.level}     Lives:{self.lives}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_text()

    def decrease_lives(self):
        self.lives -= 1
        self.update_text()

    def game_over(self):
        self.home()
        self.write(arg="Game Over", align="center", font=FONT)
