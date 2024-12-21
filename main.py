import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
game_is_on = True

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.left, key='Left')

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Food & Snake collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        scoreboard.update_scoreboard()


screen.exitonclick( )