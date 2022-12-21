from turtle import Screen, Turtle
import random
from car_manager import COLORS

# Create and register spaceship shape
screen = Screen()
shape = ((0,0), (-5,0), (-6,8), (-14,8), (-15,0), (-20,0), (-15,-12), (-5,-12))
screen.register_shape("spaceship", shape)

# Global variables
SPACESHIP_MOVE_DISTANCE = 15
SPACESHIP_MOVE_INCREMENT = 2


class SpaceshipManager():
    def __init__(self):
        self.all_spaceship = []
        self.speed = SPACESHIP_MOVE_DISTANCE
    
    def create_ship(self):
        random_chance = random.randint(1, 50)
        if random_chance == 1:
            new_ship = Turtle("spaceship")
            new_ship.penup()
            new_ship.shapesize(stretch_wid=2, stretch_len=1)
            new_ship.color(random.choice(COLORS))
            random_y = random.randint(-240,280)
            new_ship.goto(300, random_y)
            # Randomizes starting movement angle. Reorients shape to upright angle.
            random_heading = random.randint(1,2)
            if random_heading == 1:
                new_ship.setheading(135)
                new_ship.settiltangle(-45)
            else:
                new_ship.setheading(225)
                new_ship.settiltangle(225)
            self.all_spaceship.append(new_ship)

    # Set the ship movement, angle and speed. Changes direction based on location
    def move_ship(self):
        for ships in self.all_spaceship:
            y_cor = Turtle.ycor(ships)
            ships.forward(self.speed)
            if y_cor >= 270:
                ships.setheading(225)
                ships.settiltangle(225)
            if y_cor <= -230:
                ships.setheading(135)
                ships.settiltangle(315)

    def increase_speed(self):
        self.speed += SPACESHIP_MOVE_INCREMENT