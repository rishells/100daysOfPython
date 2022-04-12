from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, INITIAL_POSITION):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.penup()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




# rPaddle = Turtle()
# rPaddle.shape("square")
# rPaddle.color("white")
# rPaddle.shapesize(5,1)
# rPaddle.penup()
# rPaddle.goto(350,0)
