from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        with open("data.txt") as file:
            self.high_score = file.read()
            self.high_score = int(self.high_score)
        self.score = -1
        self.hideturtle()
        self.color("Blue")
        self.setpos(-100,280)
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.high_score}", False,  font=("Arial", 15, "normal"))

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as highscore:
                highscore.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()