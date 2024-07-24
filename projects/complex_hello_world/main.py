"""
Complex version of traditional "Hello World" (just for fun)
"""
import time
from random import choice, shuffle
import base64


def take_time(hello_function, convert_to_nanoseconds=False):
    start_time = time.perf_counter()
    hello_function()
    end_time = time.perf_counter()
    time_spent = end_time - start_time

    if convert_to_nanoseconds:
        time_spent_nanoseconds = time_spent * (10 ** 9)
        print(f"Time spent: {int(time_spent_nanoseconds)} nanoseconds")
    else:
        print(f"Time spent: {int(time_spent)} seconds")


def good_way():
    print("Hello World! (Good)")


def bad_way(should_run=False, should_decode=False):
    if not should_run:
        return bad_way(choice([True, False]), choice([True, False]))

    with open("hello_b64.txt", "r") as file:
        hello_b64 = file.read()
        if not should_decode:
            return bad_way(choice([True, False]), choice([True, False]))

        hello_str = base64.b64decode(hello_b64).decode('utf-8')

        while hello_str != "hello world":
            hello_list = list(hello_str)
            shuffle(hello_list)
            hello_str = ''.join(hello_list)

        print(f"{hello_str} (Bad Way)")


if __name__ == '__main__':
    print("--Good Way--")
    take_time(good_way, True)
    print("--Bad Way--")
    take_time(bad_way)
