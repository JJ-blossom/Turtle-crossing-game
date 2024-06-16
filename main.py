# noinspection PyInterpreter
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
COUNT = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()
    COUNT += 1
    # GENERATE NEW CAR EVERY 6 SECONDS
    if COUNT == 6:
        car_manager.create_car()
        COUNT = 0
    # DETECT IF PLAYER HIT BY CAR
    for car in car_manager.car_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    # DETECT PLAYER LEVEL COMPLETE
    if player.ycor() >= 270:
        player.reset()
        car_manager.increase_speed()
        scoreboard.next_level()


screen.exitonclick()




