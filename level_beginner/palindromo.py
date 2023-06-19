"""
Definir una función es_palindromo() que reconoce palíndromos
(es decir, palabras que tienen el mismo aspecto escritas invertidas)
"""

from inversa import inversa


def es_palindromo(string: str):
    return string == inversa(string)


if __name__ == '__main__':
    print(es_palindromo("ala"))
    print(es_palindromo("estrato"))
    print(es_palindromo("amor"))
    print(es_palindromo("oro"))
