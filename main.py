import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food.xcor(), food.ycor()) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    if snake.head.xcor() >= 295 or snake.head.xcor() <= -295 or snake.head.ycor() >= 295 or snake.head.ycor() <= -295:
        scoreboard.reset()
        snake.reset()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg.xcor(), seg.ycor()) < 10:
            scoreboard.reset()
            snake.reset()
            break

screen.exitonclick()