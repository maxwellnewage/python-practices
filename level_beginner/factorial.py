"""
Definir una función que genere un resultado del factorial de un número
Explicación función factorial: https://factorialhr.ar/numero-funcion-factorial
"""


def factorial(n):
    # se ha acordado que en el caso de 0 factorial el resultado será igual a 1
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial(7))
    print(factorial(3))
    print(factorial(1))
    print(factorial(0))
