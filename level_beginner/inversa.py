"""
Definir una función inversa() que calcule la inversión de una cadena.
"""


def inversa(string: str):
    reversed_string = ""
    for s in range(len(string), 0, -1):
        reversed_string += string[s-1]
    return reversed_string


if __name__ == '__main__':
    print(inversa("Hola"))
