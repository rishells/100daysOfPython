from turtle import Turtle, Screen, xcor
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


R_PADDLE_POSITION = (350,0)
L_PADDLE_POSITION = (-350,0)

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle(R_PADDLE_POSITION)
l_paddle = Paddle(L_PADDLE_POSITION)
ball = Ball()
scoreboard = Scoreboard()

# def up(): 
#     new_y = r_paddle.ycor() + 20
#     r_paddle.goto(r_paddle.xcor(), new_y)

# def down():
#     new_y = rPaddle.ycor() - 20
#     rPaddle.goto(rPaddle.xcor(), new_y)


screen.listen()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

speed = 0
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # Detect when R paddle misses
    if ball.xcor() > 380:
        # ball.bounce_x()
        # ball.home()
        ball.reset_position() # replaced for the 2 methods above
        scoreboard.l_point()
        # ball.speed(speed)
        # speed+=1
        
    # Detect when L paddle misses
    if ball.xcor() < -380:
        # ball.bounce_x()
        # ball.home()
        ball.reset_position() # replaced for the 2 methods above
        scoreboard.r_point()

screen.exitonclick()