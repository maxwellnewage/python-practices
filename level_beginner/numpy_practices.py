"""
Prácticas en numpy
"""

from sys import getsizeof
from random import randint
import numpy as np
import matplotlib.pyplot as plt


def print_types():
    print(f"Tipo: {type(10)} | Tamaño: {getsizeof(10)} bytes")

    np_int = np.int8(10)
    print(f"Tipo: {np.dtype(np_int)} | Tamaño: {np.dtype(np_int).itemsize} bytes")

    print(f"Tipo: {type([1, 2, 3])} | Tamaño: {getsizeof([1, 2, 3])} bytes")

    np_array = np.array([1, 2, 3])
    print(f"Tipo: {np_array.dtype} | Tamaño: {np_array.nbytes} bytes")


def list_np_array():
    py_multi_list = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    np_multi_array = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    print(
        f"Tipo: {type(py_multi_list)} | Tamaño: {getsizeof(py_multi_list)} bytes"
    )
    print(
        f"Tipo: {np_multi_array.dtype} | Tamaño: {np_multi_array.nbytes} bytes"
    )


def plot_noise():
    noise = np.random.random((128, 128, 3))
    print(noise)
    plt.imshow(noise)
    plt.pause(0.5)


if __name__ == '__main__':
    for _ in range(5):
        plot_noise()
