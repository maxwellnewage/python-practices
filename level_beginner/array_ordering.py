"""
Ordenar dos arrays enteros de forma ascendente
"""


def order_arrays(a, b):
    c = []
    pos_a = pos_b = 0

    # recorro ambos arrays
    while pos_a < len(a) and pos_b < len(b):
        # verifico el menor valor para insertarlo primero
        if a[pos_a] < b[pos_b]:
            c.append(a[pos_a])
            pos_a += 1
        else:
            c.append(b[pos_b])
            pos_b += 1

    # agrego el resto de los elementos a la lista
    c.extend(a[pos_a:])
    c.extend(b[pos_b:])

    return c


if __name__ == '__main__':
    a = [1, 2, 5]
    b = [3, 4, 6]
    print(order_arrays(a, b))
