import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

<<<<<<< HEAD
=======
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")

>>>>>>> c9d687b9a5d70c283e71f43cac9fe2b7d7edc811
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
<<<<<<< HEAD
=======

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        #screen.update()

screen.exitonclick()
>>>>>>> c9d687b9a5d70c283e71f43cac9fe2b7d7edc811
