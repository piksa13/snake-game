from turtle import Turtle

MOVE_DISTANCE = 20
SNAKE_SIZE = 3
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.x_position = 0
        self.y_position = 0
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for _ in range(SNAKE_SIZE):
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(self.x_position, self.y_position)
            self.snake.append(segment)
            self.x_position = segment.xcor() - 20


    def move(self):
        for segment_index in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment_index - 1].xcor()
            new_y = self.snake[segment_index - 1].ycor()
            self.snake[segment_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)