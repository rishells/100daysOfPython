# import colorgram

# rgb_colors = []
# colors = colorgram.extract('day18\hirst-painting\image.jpg',30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)


#from turtle import Turtle, Screen, colormode
from turtle import Screen
import random
import turtle as t 


screen = Screen()
tim = t.Turtle()
# Turtle object properties
t.colormode(255)
t.shape("turtle")
t.speed(0)
t.pensize(2)


color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 
66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]


i = 0
for _ in range (10):
    
    t.pu()
    t.setposition(-300,(-300 + i))
    t.pd()
    i+=50

    for _ in range (10):
        t.dot(20,color_list[random.randrange(0,len(color_list))])
        t.pu()
        t.fd(50)
        t.pd()
    
    

# t.pu()
# t.setposition(-300,-260)
# t.pd()

# for _ in range (10):
#     t.dot(20,color_list[random.randrange(0,len(color_list))])
#     t.pu()
#     t.fd(50)
#     t.pd()



screen.exitonclick()

