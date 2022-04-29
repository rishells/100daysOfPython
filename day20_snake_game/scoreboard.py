from turtle import Turtle
ALIGNMENT = "center"
FONT =  ("Arial", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.high_score = self.get_score()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
        
    def get_score(self):
        with open("day20_snake_game\data.txt") as score_data:
            score = score_data.read()
            return int(score)
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",False, align=ALIGNMENT, font=FONT)

        
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day20_snake_game\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)