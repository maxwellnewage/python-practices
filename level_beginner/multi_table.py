"""
Para un número N imprimir su tabla de multiplicar.
"""


def multi_table(num):
    print(f"Tabla de multiplicar de {num}")
    for n in range(11):
        print(f"{n} x {num} = {n * num}")
    print("------------------------------")


if __name__ == '__main__':
    multi_table(2)
    multi_table(4)
    multi_table(5)
