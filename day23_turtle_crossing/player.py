<<<<<<< HEAD
=======
from turtle import Turtle


>>>>>>> c9d687b9a5d70c283e71f43cac9fe2b7d7edc811
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


<<<<<<< HEAD
class Player:
    pass
=======
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.seth(90)
        self.penup()
        self.go_to_start()

    def go_up(self):
        # new_y = self.ycor() + 20
        # self.goto(self.xcor(),new_y)
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
            
>>>>>>> c9d687b9a5d70c283e71f43cac9fe2b7d7edc811
