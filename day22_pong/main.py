from turtle import Turtle, Screen
from paddle import Paddle


R_PADDLE_POSITION = (350,0)
L_PADDLE_POSITION = (-350,0)

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(R_PADDLE_POSITION)
l_paddle = Paddle(L_PADDLE_POSITION)

# def up(): 
#     new_y = r_paddle.ycor() + 20
#     r_paddle.goto(r_paddle.xcor(), new_y)

# def down():
#     new_y = rPaddle.ycor() - 20
#     rPaddle.goto(rPaddle.xcor(), new_y)


screen.listen()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")


game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()