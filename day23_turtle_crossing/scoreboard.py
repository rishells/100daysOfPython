<<<<<<< HEAD
FONT = ("Courier", 24, "normal")


class Scoreboard:
    pass
=======
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290,250)
        self.update_score_board()
        
    def update_score_board(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score_board()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER! ", align="center", font=FONT)


        
>>>>>>> c9d687b9a5d70c283e71f43cac9fe2b7d7edc811
