import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

car_speed = 0.1


screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(car_speed)
    screen.update()
    cars.move_cars()
    for car in cars.car_list:
        if car.distance(player) < 20:
            player.reset_player()
            cars.place_cars_at_start()
            scoreboard.decrease_lives()
    if player.ycor() > 280:
        player.reset_player()
        cars.place_cars_at_start()
        car_speed *= 0.9
        scoreboard.increase_level()
    if scoreboard.lives == 0:
        scoreboard.game_over()
        game_is_on = False
screen.exitonclick()
