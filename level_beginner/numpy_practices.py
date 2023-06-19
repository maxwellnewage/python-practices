"""
Prácticas en numpy
"""

from sys import getsizeof
import numpy as np


print(f"Tipo: {type(10)} | Tamaño: {getsizeof(10)} bytes")

np_int = np.int8(10)
print(f"Tipo: {np.dtype(np_int)} | Tamaño: {np.dtype(np_int).itemsize} bytes")

print(f"Tipo: {type([1, 2, 3])} | Tamaño: {getsizeof([1, 2, 3])} bytes")

np_array = np.array([1, 2, 3])
print(f"Tipo: {np_array.dtype} | Tamaño: {np_array.nbytes} bytes")

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
