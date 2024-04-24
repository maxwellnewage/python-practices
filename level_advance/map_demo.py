def make_even(num):
    if num % 2 == 1:
        return num + 1
    else:
        return num


if __name__ == '__main__':
    nums = list(range(51))

    even_nums_map = map(make_even, nums)
    print(even_nums_map)

    even_nums = list(even_nums_map)
    print(even_nums)
