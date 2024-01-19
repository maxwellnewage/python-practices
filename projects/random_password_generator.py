"""
Generador de contraseñas.
Basado en https://youtu.be/qgwEs36D_Xc
"""

import random


def set_char_upper_or_lower(char: str):
    choice = random.choice(range(0, 2))
    return char.upper() if choice == 0 else char.lower()


def generate_pw(pw_len=10, pw_count=1):
    chars = "abcdefghijklmnopqrstuvwxyz123456!$%^(*)"
    password_list = []

    for _ in range(0, pw_count):
        password = ""
        for _ in range(0, pw_len):
            pw_char = set_char_upper_or_lower(random.choice(chars))
            password += pw_char
        password_list.append(password)
    return password_list


if __name__ == '__main__':
    input_pw_len = int(input("Que tamaño de contraseña quieres?: "))
    input_pw_count = int(input("Cuantas contraseñas te gustaría generar?: "))

    pw_list = generate_pw(input_pw_len, input_pw_count)
    for i, pw in enumerate(pw_list):
        print(f"Password #{i + 1}: {pw}")

    print(generate_pw()[0])
