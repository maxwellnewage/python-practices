"""
Validar si un email es correcto
"""
import re


def validate_email(email):
    return re.compile(r'''
        [a-zA-Z0-9_.+]+  # name part
        @                # @ symbol
        [a-zA-Z0-9_.+]+  # domain part before dot
        \.\w+          # domain part after dot
        ''', re.VERBOSE).search(email)


if __name__ == '__main__':
    # good cases
    print(validate_email("tomas@mail.com"))
    print(validate_email("to.mas@mail.com"))
    print(validate_email("to_mas@mail.com"))

    # bad cases
    print(validate_email("to.mas@mail"))
    print(validate_email("to.masmail.com"))
    print(validate_email("to.mas+mail.com"))
