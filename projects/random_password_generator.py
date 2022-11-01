"""
Generador de contraseñas.
Basado en https://youtu.be/qgwEs36D_Xc
"""

import random


def set_char_upper_or_lower(char: str):
    choice = random.choice(range(0, 2))
    return char.upper() if choice == 0 else char.lower()


def generate_pw():
    chars = "abcdefghijklmnopqrstuvwxyz123456!$%^(*)"
    password_list = []
    pw_len = int(input("Que tamaño de contraseña quieres?: "))
    pw_count = int(input("Cuantas contraseñas te gustaría generar?: "))

    for _ in range(0, pw_count):
        password = ""
        for _ in range(0, pw_len):
            pw_char = set_char_upper_or_lower(random.choice(chars))
            password += pw_char
        password_list.append(password)
    return password_list


pw_list = generate_pw()
for i, pw in enumerate(pw_list):
    print(f"Password #{i+1}: {pw}")
