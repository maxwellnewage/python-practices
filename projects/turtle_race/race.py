from random import randint
from turtle import Turtle

from projects.turtle_race.score import Score


class Race:
    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtles = []
    SCREEN_SCALE = 0
    __is_race_on = False

    def __init__(self, screen_scale):
        self.SCREEN_SCALE = screen_scale
        self.y_pos = [float(x) * screen_scale for x in [-70, -40, -10, 20, 50, 80]]

    def __put_turtles(self):
        for index in range(0, 6):
            turtle = Turtle(shape="turtle")
            turtle.penup()
            turtle.color(self.COLORS[index])
            turtle.goto(-230 * self.SCREEN_SCALE, self.y_pos[index])
            self.turtles.append(turtle)

    def move_turtles(self, user_bet: str, text_result: Score, text_winner_turtle: Score):
        while self.is_racing():
            for turtle in self.turtles:
                if turtle.xcor() > 230 * self.SCREEN_SCALE:
                    if turtle.pencolor() == user_bet:
                        text_result.color("blue")
                        text_result.write_result("You've won!")
                    else:
                        text_result.color("red")
                        text_result.write_result("You've lost!")

                    text_winner_turtle.write_result(f"Winner turtle: {turtle.pencolor()}")

                    self.__is_race_on = False

                rand_distance = randint(0, 10)
                turtle.forward(rand_distance)

    def start(self):
        self.__put_turtles()
        self.__is_race_on = True

    def is_racing(self):
        return self.__is_race_on
