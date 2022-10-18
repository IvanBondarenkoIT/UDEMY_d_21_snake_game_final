from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Scoore

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

score = Scoore()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect colision with the snake
    if snake.head.distance(food) < 15:
        food.refrash()
        snake.extend()
        score.refrash_score()

    # Detect colision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.xcor() < -290:
        game_is_on = False
        score.game_ower()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_ower()

screen.exitonclick()