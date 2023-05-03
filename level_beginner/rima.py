"""
Escribe un programa que pida dos palabras y diga si riman o no.
Si coinciden las tres últimas letras tiene que decir que riman.
Si coinciden solo las dos últimas tiene que decir que riman un poco y si no, que no riman.
"""


def rima(first_word: str, second_word: str):
    if first_word[::-1][0:3] == second_word[::-1][0:3]:
        return "las palabras riman!"
    elif first_word[::-1][0:2] == second_word[::-1][0:2]:
        return "las palabras riman un poco..."
    else:
        return "las palabras no riman."


if __name__ == '__main__':
    print(rima("casa", "sa"))
    print(rima("plaza", "maza"))
    print(rima("taza", "raza"))
    print(rima("caos", "puente"))
