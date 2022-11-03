from movement import Movement
from hud import HUD
from food import Food

import turtle
import time
import random


class Snake(Movement):

    def __init__(self):
        # Direcciones
        self.DIRECTION_STOP = "stop"
        self.DIRECTION_UP = "up"
        self.DIRECTION_DOWN = "down"
        self.DIRECTION_LEFT = "left"
        self.DIRECTION_RIGHT = "right"

        # Cola de la serpiente
        self.snake_parts = []

        # HUD
        self.hud = HUD()

        # Food
        self.food = Food()

        # Cabeza de la serpiente
        self.__head = turtle.Turtle()
        self.__head.speed(0)
        self.__head.shape("square")
        self.__head.color("white")
        self.__head.penup()
        self.__head.goto(0, 0)
        self.__head.direction = self.DIRECTION_STOP

    def get_snake_head(self):
        return self.__head

    def move_up(self):
        self.__head.direction = self.DIRECTION_UP

    def move_down(self):
        self.__head.direction = self.DIRECTION_DOWN

    def move_left(self):
        self.__head.direction = self.DIRECTION_LEFT

    def move_right(self):
        self.__head.direction = self.DIRECTION_RIGHT

    def move(self):
        if self.__head.direction == self.DIRECTION_UP:
            y = self.__head.ycor()
            self.__head.sety(y + 20)

        if self.__head.direction == self.DIRECTION_DOWN:
            y = self.__head.ycor()
            self.__head.sety(y - 20)

        if self.__head.direction == self.DIRECTION_LEFT:
            x = self.__head.xcor()
            self.__head.setx(x - 20)

        if self.__head.direction == self.DIRECTION_RIGHT:
            x = self.__head.xcor()
            self.__head.setx(x + 20)

    def reset_snake_body(self):
        for parts in self.snake_parts:
            parts.hideturtle()
        self.snake_parts.clear()
        self.__head.goto(0, 0)
        self.__head.direction = self.DIRECTION_STOP
        self.hud.reset_score()

    def __create_snake_part(self):
        snake_part = turtle.Turtle()
        snake_part.speed(0)
        snake_part.shape("square")
        snake_part.color("grey")
        snake_part.penup()
        return snake_part

    def move_all_snake_parts(self):
        snake_parts_size = len(self.snake_parts)
        for part in range(snake_parts_size - 1, 0, -1):
            x = self.snake_parts[part - 1].xcor()
            y = self.snake_parts[part - 1].ycor()
            self.snake_parts[part].goto(x, y)

        if snake_parts_size > 0:
            x = self.__head.xcor()
            y = self.__head.ycor()
            self.snake_parts[0].goto(x, y)

    def detect_border_collision(self):
        if self.__head.xcor() > 290 or \
                self.__head.xcor() < -290 or \
                self.__head.ycor() > 290 or \
                self.__head.ycor() < -290:
            time.sleep(0.5)
            self.reset_snake_body()

    def detect_food_collision(self):
        if self.__head.distance(self.food.get_food()) < 20:
            self.food.respawn_food()

            snake_part = self.__create_snake_part()
            self.snake_parts.append(snake_part)
            self.hud.increment_score(10)

    def detect_snake_parts_collision(self):
        for part in self.snake_parts:
            if part.distance(self.__head) < 20:
                time.sleep(0.5)
                self.reset_snake_body()
