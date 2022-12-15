import time
from turtle import Screen, Turtle
# Statements to import classes from local files
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # has everything not start at 0, 0 and move to its starting position

# Create our objects to manipulate
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listens for any inputs we give
screen.listen()
# Sets it so we run the move_method whenever the Up key is entered
# ? Left/Right Movement?
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_forward, "w")


game_is_on = True
while game_is_on:
    # Keeps the program from running too fast
    time.sleep(0.1)
    # Keeps the screen updating
    screen.update()

    # Creates the obstacles
    car_manager.create_car()

    # Moves the obstacles
    car_manager.move_cars()
    
    # If someone finishes, reset the level
    if player.crossed_finish():
        player.reset_turtle()
        scoreboard.increase_level()
        car_manager.increase_speed()

    # Ends game on collision
    for car in car_manager.all_cars:
        if car.distance(player) < 19:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()