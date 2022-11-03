"""
Juego de la serpiente.
"""

import time

from window_manager import WindowManager
from snake import Snake


def play():
    window = WindowManager()
    snake = Snake()
    window.set_events(snake)

    while True:
        window.get_window().update()

        snake.detect_border_collision()
        snake.detect_food_collision()
        snake.detect_snake_parts_collision()

        snake.move_all_snake_parts()
        snake.move()

        time.sleep(0.1)


if __name__ == '__main__':
    play()
