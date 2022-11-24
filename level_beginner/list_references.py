"""
Ejemplo que demuestra como funcionan las listas por referencia
"""

list_a = [1, 2, 3]
print(list_a)

# pasaje de valores por referencias
list_b = list_a
# cambian ambas listas
list_b[0] = 5
print(list_a, list_b)

# copia una lista en otra
list_c = list(list_a)
# cambia solo la lista list_c
list_c[0] = 10
print(list_a, list_c)
