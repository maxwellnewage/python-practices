"""
Escribir un programa que le diga al usuario que ingrese una cadena.
El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

string = input("Ingresa una cadena: ")
upper_chars = 0

for s in string:
    if s.isupper():
        upper_chars += 1

print(f"Tu cadena tiene {upper_chars} caracteres en mayúscula.")
