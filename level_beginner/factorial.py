"""
Definir una función que genere un resultado del factorial de un número
"""


def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0  # evita un desborde de recursión
    else:
        return n * factorial(n - 1)


print(factorial(7))
print(factorial(3))
print(factorial(1))
print(factorial(0))
