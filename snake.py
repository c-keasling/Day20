from turtle import Screen, Turtle
import time
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self,game_is_on = True):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_snake = Turtle("square")
        new_snake.penup()
        new_snake.color('white')
        new_snake.goto(position)
        self.snake_parts.append(new_snake)

    def reset(self):
        for seg in self.snake_parts:
            seg.goto(1000,1000)
        self.snake_parts.clear()
        self.create_snake()
        self.head = self.snake_parts[0]

    def extend(self):
        self.add_segment(self.snake_parts[-1].position())

    def moving(self):
            for parts in range(len(self.snake_parts) - 1, 0, -1):
                new_x = self.snake_parts[parts - 1].xcor()
                new_y = self.snake_parts[parts - 1].ycor()
                self.snake_parts[parts].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
