from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(COLORS))
        start_y = randint(-250, 250)
        new_car.goto(280, start_y)
        new_car.setheading(180)
        new_car.speed(MOVE_INCREMENT)
        self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            if car.xcor() > -350:
                car.forward(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT

