from turtle import Turtle
import random

# ! Inactive: River/Log. Check main.py for reinstalling

class RiverManager():
    def __init__(self):
        river = Turtle("square")
        river.penup()
        river.shapesize(stretch_wid=2, stretch_len=36)
        river.color("blue")
        river.goto(0, 100)
        # ? Might be unneeded. Will require an array to put into otherwise.
        # self.location.append(river)