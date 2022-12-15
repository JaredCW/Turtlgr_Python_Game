from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        print("Creating scoreboard")
        # Starting level will be one
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-250, 250)
        self.hideturtle()
        self.update_scoreboard()

    # Update the scoreboard
    def update_scoreboard(self):
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    # What happens when the game is over?
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER. You reached level {self.level}.", move=False, align="center", font=FONT)

    # Increment the level whenever player makes it to the end
    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()