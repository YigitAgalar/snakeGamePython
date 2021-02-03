from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.color("Blue")
        self.setpos(-40,280)
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False,  font=("Arial", 15, "normal"))

    def game_over(self):

        self.color("Red")
        self.goto(-100, -10)
        self.write("Game Over.", False, font=("Arial", 30, "normal"))
