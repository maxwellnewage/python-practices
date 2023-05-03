"""
Identificar si la suma de los dígitos de un número es par o impar.
"""


def par_impar(n1: str):
    # devuelvo lista de n casteado a int recorriendo n1
    num_list = [int(n) for n in n1]
    sum_num = 0
    for n in num_list:
        sum_num += n
    return sum_num % 2 == 0


if __name__ == '__main__':
    number = input("Introduce un numero: ")
    print(par_impar(number))
