"""
Definir una función max_num_three(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""

from max_number import max_num


def max_num_three(n1, n2, n3):
    res = max_num(n1, n2)
    return res if res > n3 else n3


print(max_num_three(1, 2, 4))
print(max_num_three(10, 5, 1))
