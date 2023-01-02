from turtle import Screen, Turtle

CURSOR_SIZE = 20
FONT_SIZE = 24
FONT = ("Courier", FONT_SIZE, "normal")


class Button_Start(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.fillcolor("red")
        self.penup()
        self.goto(150, 150)
        self.write("START", align='center', font=FONT)
        self.sety(150 + CURSOR_SIZE + FONT_SIZE)
        self.showturtle()

    def start_game(self):
        self.hideturtle()
