"""
Definir una función max_num() que tome como argumento
dos números y devuelva el mayor de ellos.
"""


def max_num(n1, n2):
    return n1 if n1 > n2 else n2


if __name__ == '__main__':
    print(max_num(1, 2))
    print(max_num(4, 1))
