from turtle import Turtle
import random


RIVER_START = random.randint(-200, 200)
RIVER_END = RIVER_START + 40

class RiverManager():
    def __init__(self):
        pass

    def create_river(self):
        river = Turtle("square")
        river.penup()
        river.shapesize(stretch_wid=2, stretch_len=36)
        river.color("blue")
        river.goto(0, RIVER_START)
        # ? Might be unneeded. Will require an array to put into otherwise.
        # self.location.append(river)