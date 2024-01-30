"""
Speed Calculator Decorator
"""

import time as t
from bad_word_detector import phrase_filter


def speed_calculator(function):
    def wrapper_function():
        start_time = t.time()
        function()
        end_time = t.time()

        print(f"{function.__name__} | run speed: {end_time - start_time}")

    return wrapper_function


@speed_calculator
def short_phrase():
    for _ in range(100*100):
        phrase_filter("Me gusta la manzana")


@speed_calculator
def long_phrase():
    for _ in range(100*100):
        phrase_filter("Me gusta la manzana, además de la pera y la banana")


if __name__ == '__main__':
    short_phrase()
    long_phrase()
