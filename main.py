import time
import snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
screen.update()
screen.listen()
snake = snake.Snake()
food = Food()
score = Scoreboard()
screen.onkey(key="Up", fun=snake.go_up)
screen.onkey(key="Down", fun=snake.go_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.moving()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

# colliding with wall

    if snake.head.xcor() >= 300:
        snake.reset()
        score.reset_scoreboard()
    elif snake.head.xcor() <= -300:
        snake.reset()
        score.reset_scoreboard()
    elif snake.head.ycor() <= -300:
        snake.reset()
        score.reset_scoreboard()
    elif snake.head.ycor() >= 300:
        snake.reset()
        score.reset_scoreboard()

# colliding with tail

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
           snake.reset()
           score.reset_scoreboard()


screen.exitonclick()