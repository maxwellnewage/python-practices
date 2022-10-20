"""
Calculadora que puede sumar, restar, multiplicar y dividir dos números
"""

ops = ['s', 'r', 'm', 'd']
op = ""

'''
utilizo la asignación múltiple de valores con un método split
para dividirlos en espacios y mantener los valores en n1 y n2
'''
n1, n2 = input("Introduce dos numeros separados por espacio: ").split()

# mientras que el operador (op) no sea válido, sigo preguntando
while op not in ops:
    op = input(
        """
        Elige una operación:
        (s)umar
        (r)estar
        (d)ividir
        (m)ultiplicar
        """)

    if op == "s":
        # utilizo string templates para imprimir las variables
        # casteo a entero porque input devuelve string
        print(f"La suma de {n1} y {n2} es {int(n1) + int(n2)}")
    elif op == "r":
        print(f"La resta de {n1} y {n2} es {int(n1) - int(n2)}")
    elif op == "d":
        print(f"La división de {n1} y {n2} es {int(n1) / int(n2)}")
    elif op == "m":
        print(f"La multiplicación de {n1} y {n2} es {int(n1) * int(n2)}")
    else:
        print("El operador escrito no es válido, vuelve a intentarlo")
