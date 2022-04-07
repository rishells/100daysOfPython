# 360 / number of sides


#from turtle import Turtle, Screen, colormode
from turtle import Screen
import random
import turtle as t 

tim = t.Turtle()
# Turtle object properties
t.colormode(255)
t.shape("turtle")
t.speed(0)
t.pensize(2)


def random_color():
    '''Returns a tuple with the random values rgb'''
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b) 




for i in range(10,370,1):
    tup = random_color() 
    t.pencolor(tup)
    t.circle(100) # Draw a circle or radius 100
    t.setheading(i) # Where the turtle is heading to
 




# for _ in range(500):
#     tup = random_color()
#     t.pencolor(tup)
#     t.forward(30)
#     t.right(random.randrange(0,360,90))




######## Draw polygons with random colors
screen = Screen()
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.speed(1)
# timmy_the_turtle.pensize(10)






# Draw polygons with different colors
# for i in range(3,11):
#     tup = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
#     timmy_the_turtle.pencolor(tup)
#     for j in range(0,i):
        
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/i)

# print(random.randint(1,255))




screen.exitonclick()


    





















# ------------------------------------------------
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()