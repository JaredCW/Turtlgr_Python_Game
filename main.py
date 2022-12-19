
import time
from turtle import Screen, Turtle
# Statements to import classes from local files
from player import Player
from car_manager import CarManager
from train_manager import TrainManager
from spaceship import SpaceshipManager
from river import RiverManager
from log_manager import LogManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # has everything not start at 0, 0 and move to its starting position

# Create our objects to manipulate
player = Player()
river_manager = RiverManager()
car_manager = CarManager()
train_manager = TrainManager()
spaceship_manager = SpaceshipManager()
log_manager = LogManager()
scoreboard = Scoreboard()

# Listens for any inputs we give
screen.listen()
# Movement keys (Up/Left/Right and WASD)
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_forward, "w")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_right, "d")
screen.onkeypress(screen.bye, "Escape")
# TODO: Create player bounds for left/right movement


# River is created outside of the game loop, as it is a static object
river_manager.__init__()

game_is_on = True
while game_is_on:
    # Keeps the program from running too fast
    time.sleep(0.1)
    # Keeps the screen updating
    screen.update()

    # Creates the obstacles
    car_manager.create_car()
    train_manager.create_train()
    spaceship_manager.create_ship()
    log_manager.create_logs()

    # Moves the obstacles
    car_manager.move_cars()
    train_manager.move_trains()
    spaceship_manager.move_ship()
    log_manager.move_logs()
    
    # If someone finishes, reset the level
    if player.crossed_finish():
        player.reset_turtle()
        scoreboard.increase_level()
        car_manager.increase_speed()
        train_manager.increase_speed()
        spaceship_manager.increase_speed()

    # Ends game on collision
    # * Collsion needs more work, especially for unique polygons (ie - Spaceship)
    for car in car_manager.all_cars:
        if car.distance(player) < 19:
            game_is_on = False
            scoreboard.game_over()

    for train in train_manager.all_trains:
        if train.distance(player) < 19:
            game_is_on = False
            scoreboard.game_over()

    for ship in spaceship_manager.all_spaceship:
        if ship.distance(player) < 19:
            game_is_on = False
            scoreboard.game_over()

    # ! NEXT STEP - Creating river collision rules
    # while river_manager.location 
    # for log in log_manager.all_logs:
    #     if not(log.distrance(player) < 19):
    #         game_is_on = False
    #         scoreboard.game_over()

screen.exitonclick()