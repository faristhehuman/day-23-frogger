from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.create_cars()
        self.place_cars_at_start()

    def create_cars(self):
        for _ in range(13):
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.color(random.choice(COLORS))
            self.car_list.append(car)

    def place_cars_at_start(self):
        ycor = 250
        for car in self.car_list:
            xcor = random.randint(-100, 600)
            car.goto((xcor, ycor))
            ycor -= 40
            print(xcor)

    def move_cars(self):
        for car in self.car_list:
            car.forward(random.randint(0, MOVE_INCREMENT))
            if car.xcor() < -320:
                xcor = 320
                ycor = car.ycor()
                car.goto((xcor, ycor))

