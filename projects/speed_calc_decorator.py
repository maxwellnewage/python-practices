"""
Speed Calculator Decorator
"""

import time as t
from bad_word_detector import phrase_filter


def speed_calculator(function):
    def wrapper_function(*args):
        start_time = t.time()
        function(*args)
        end_time = t.time()

        print(f"{function.__name__} | run speed: {end_time - start_time} | called {args[0]} times")

    return wrapper_function


@speed_calculator
def short_phrase(times: int):
    for _ in range(times):
        phrase_filter("Me gusta la manzana")


@speed_calculator
def long_phrase(times: int):
    for _ in range(times):
        phrase_filter("Me gusta la manzana, además de la pera y la banana")


if __name__ == '__main__':
    short_phrase(100*1000)
    long_phrase(100*100)
