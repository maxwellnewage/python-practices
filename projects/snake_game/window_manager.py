import turtle
from movement import Movement


class WindowManager:
    def __init__(self):
        self.__window = turtle.Screen()
        self.__window.title("Pong")
        self.__window.bgcolor("black")
        self.__window.setup(width=600, height=600)
        self.__window.tracer(0)

    def get_window(self):
        return self.__window

    def set_events(self, movement: Movement):
        self.__window.listen()
        self.__window.onkeypress(movement.move_up, "Up")
        self.__window.onkeypress(movement.move_down, "Down")
        self.__window.onkeypress(movement.move_left, "Left")
        self.__window.onkeypress(movement.move_right, "Right")
