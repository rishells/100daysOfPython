from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
   

        
        


# Iterating with objects and assigning them position to create the initial snake of the squares

# x_positions=[0,-20,-40]
# all_turtles = []
# for turtle_index in range(0,3):
#     new_turtle = Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.penup()
#     new_turtle.goto(x=x_positions[turtle_index],y=0)
#     all_turtles.append(new_turtle)

screen.exitonclick()

