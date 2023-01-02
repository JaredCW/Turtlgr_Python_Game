
import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager, STARTING_MOVE_DISTANCE
from train_manager import TrainManager, TRAIN_MOVE_DISTANCE
from spaceship import SpaceshipManager, SPACESHIP_MOVE_DISTANCE
from river import RiverManager, RIVER_START, RIVER_END
from log_manager import LogManager
from scoreboard import Scoreboard

FONT = ("Courier", 24, "normal")

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # has everything not start at 0, 0 and move to its starting position

# Assigns variables to each imported class.
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
# Exit game key
screen.onkeypress(screen.bye, "Escape")
# ? Create player bounds for left/right movement?

game_is_on = True
# TODO: Working on Start button prior to start. How to draw a Turtle button that gets removed and starts the game_is_on loop?
# game_is_on = False

# def button_start(Turtle):
#     button = Turtle()
#     button.hideturtle()
#     button.shape('circle')
#     button.fillcolor('red')
#     button.penup()
#     button.goto(150, 150)
#     button.write("START", align='center', font=FONT)
#     button.sety(150 + 20 + 24)
#     button.onclick(draw_onclick)
#     button.showturtle()

# Button_Start.__init__(Turtle)
# if game_is_on == True:
#     Button_Start.start_game()

while game_is_on:
    # Keeps the program from running too fast
    time.sleep(0.1)
    # Keeps the screen updating
    screen.update()

    # Creates the obstacles (uses imported class variables!)
    car_manager.create_car()
    # * NEW: Introduce new obstables in later levels.
    if scoreboard.level >= 5:
        train_manager.create_train()
    if scoreboard.level >= 8:
        spaceship_manager.create_ship()
    river_manager.create_river()
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
        # * NEW: This resets the speed of the obstacles at the levels where new ones are introduced.
        # ? Should I define more functions in the other files to run these?
        if scoreboard.level == 5:
            car_manager.speed = STARTING_MOVE_DISTANCE
            train_manager.speed = TRAIN_MOVE_DISTANCE
        if scoreboard.level == 8:    
            car_manager.speed = STARTING_MOVE_DISTANCE
            train_manager.speed = TRAIN_MOVE_DISTANCE
            spaceship_manager.speed = SPACESHIP_MOVE_DISTANCE

    # Ends game on collision
    # TODO **PRIORITY**: Collsion needs more work, especially for unique polygons (ie - Spaceship)
    # * Started new collision rules. This is almost right, but I need to math this out right. Get some graph paper and write this all out in detail, I think.
    for car in car_manager.all_cars:
        x = 0
        y = 0
        while x <= 40:
            while y <= 20:
                if ((player.xcor() - (car.xcor() + x) >= 20) and (player.ycor() - (car.ycor() + y) >= 20)):
                    game_is_on = False
                    scoreboard.game_over()
                y += 1
            x += 1

    # ! Train is too long; you don't collide with the right end.
    for train in train_manager.all_trains:
        if (train.distance(player.xcor() + x, player.ycor() + y) < 0):
            game_is_on = False
            scoreboard.game_over()

    for ship in spaceship_manager.all_spaceship:
        if ship.distance(player) < 19:
            game_is_on = False
            scoreboard.game_over()
    
    # ! This isn't working right. I'm on the right track (WHILE loop is functional), but this is likely to keep breaking until collision rules are fixed.
    while (player.ycor() >= (RIVER_START- 10) and player.ycor() <= RIVER_END):
        for log in log_manager.all_logs:
            if not(log.distance(player) < 29):
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()