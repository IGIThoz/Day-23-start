import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("white")
screen.title("Crossing Capstone")
screen.tracer(0)
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up,"Up")
game_on = True


while game_on:
    time.sleep(0.1)
    screen.update()
    # create Cars:
    car_manager.create_new_car()
    car_manager.move_cars()
    #detect car turtle
    for car in car_manager.cars:
        if car.distance(player) <20:
            game_on = False
            scoreboard.game_over()
    # Check Finish
    if player.is_fisnish() == True:

        player.go_to_start()
        car_manager.level_up()
        scoreboard.update_score()







screen.exitonclick()