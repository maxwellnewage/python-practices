"""
Unpacking example with *args
"""


def sum_nums(n1, n2, n3):
    return n1 + n2 + n3


def sum_nums_args(*args):
    return sum(args)


if __name__ == '__main__':
    nums = [4, 6, 8]

    print(sum_nums(*nums))
    print(sum_nums_args(4, 9, 10))

