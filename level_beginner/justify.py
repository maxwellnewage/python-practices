"""
Se modifica un string para agregar espacios y justificados.
"""

# justificado izquierdo y derecho
print("Hola".ljust(10))
print("Hola".rjust(10))

# justificado centrado estilo titulo
print("Titulo".center(20, "-"))
print("Titulo".center(20, "="))

# versión sin center
lines = "-" * 7
print(lines + "Titulo" + lines)
