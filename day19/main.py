from turtle import Turtle, Screen
import random
import turtle


screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner! ")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner! ")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



# def move_forwards():
#     tim.fd(100)

# def move_backwards():
#     tim.bk(100)

# def clear_drawings():
#     tim.home()
#     tim.clear()

# def move_clockwise():
#     tim.right(15)

# def move_counterclockwise():
#     tim.left(15)

# screen.listen()
# screen.onkey(key="w",fun=move_forwards)
# screen.onkey(key="s",fun=move_backwards)
# screen.onkey(key="c",fun=clear_drawings)
# screen.onkey(key="d",fun=move_clockwise)
# screen.onkey(key="a",fun=move_counterclockwise)



screen.exitonclick()  