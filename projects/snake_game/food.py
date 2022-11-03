import turtle
import random


class Food:
    def __init__(self):
        self.__food = turtle.Turtle()
        self.__food.speed(0)
        self.__food.shape("circle")
        self.__food.color("red")
        self.__food.penup()
        self.__food.goto(0, 100)

    def get_food(self):
        return self.__food

    def respawn_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.__food.goto(x, y)
