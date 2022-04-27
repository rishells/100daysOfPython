from turtle import Screen, Turtle
import time
from scoreboard import Scoreboard
from food import Food
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food with distance method 
    
    if snake.head.distance(food) < 15: # based on the food size, 10 x 10
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        scoreboard.reset()
        snake.reset()
        #game_is_on = False
        #scoreboard.game_over()
        
    # Detect collision with own tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # game_is_on = False
            # scoreboard.game_over()

     # Detect collision with own tail with slicing solution
    # for segment in snake.segments[1:]:
    #     if snake.head.distance(segment) < 10:
            #game_is_on = False
            #scoreboard.game_over()
    # If head collides with any segment in the tail:
        # trigger game_over

    
   

        
        


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

