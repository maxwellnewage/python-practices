"""
Detectar si una cadena empieza y termina con un determinado valor
"""
import re


def detect_start_str(phrase):
    return re.compile(r'^Hi').search(phrase)


def detect_end_str(phrase):
    return re.compile(r'World$').search(phrase)


def detect_both_str(phrase):
    return re.compile(r'^Hi\sWorld$').search(phrase)


def detect_both_digit_str(phrase):
    return re.compile(r'^\d+\s\w+$').search(phrase)


if __name__ == '__main__':
    print(detect_start_str("Buenas!"))
    print(detect_start_str("Hi"))
    print(detect_end_str("something World"))
    print(detect_both_str("Hi World"))
    print(detect_both_digit_str("10 Dogs"))
