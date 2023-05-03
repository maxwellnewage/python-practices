"""
Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
"""


def max_in_list(list_numbers):
    max_num = list_numbers[0]
    for n in list_numbers:
        if n > max_num:
            max_num = n
    return max_num


if __name__ == '__main__':
    print(max_in_list([1, 3, 5]))
    print(max_in_list([1, 3, 5, 7, 9]))
    print(max_in_list([1, 3, 10, 7, 9]))
