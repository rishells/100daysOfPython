<<<<<<< HEAD
=======
from turtle import Turtle
import random

>>>>>>> c9d687b9a5d70c283e71f43cac9fe2b7d7edc811
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


<<<<<<< HEAD
class CarManager:
    pass
=======
class CarManager: # Removed the  CarManager(Turtle) inheritance
    def __init__(self ):
        #super().__init__()
        # self.shape("square")
        # self.shapesize(2,4,1)
        # self.penup()
        # self.color(random.choice(COLORS))
        # self.goto(200,random.randint(-200,200))
        # self.setheading(180)
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        # new_x = self.xcor() - STARTING_MOVE_DISTANCE
        # new_y = self.ycor() + self.y_move
        # self.goto(new_x, new_y)
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
    
>>>>>>> c9d687b9a5d70c283e71f43cac9fe2b7d7edc811
