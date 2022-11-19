"""
Prácticas en numpy
"""
import array
from sys import getsizeof
import numpy as np


print(f"Tipo: {type(10)} | Tamaño: {getsizeof(10)} bytes")

print(f"Tipo: {type(np.int8(10))} | Tamaño: {getsizeof(np.int8(10))} bytes")

print(f"Tipo: {type(array.array('i', [1, 2, 3]))} | Tamaño: {getsizeof([1, 2, 3])} bytes")

print(f"Tipo: {type(np.array([1, 2, 3]))} | Tamaño: {getsizeof(np.array([1, 2, 3]))} bytes")

py_multi_list = [
    [1, 2, 3],
    [4, 5, 6]
]

np_multi_array = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(f"Tipo: {type(py_multi_list)} | Tamaño: {getsizeof(py_multi_list)} bytes")
print(f"Tipo: {type(np_multi_array)} | Tamaño: {getsizeof(np_multi_array)} bytes")
