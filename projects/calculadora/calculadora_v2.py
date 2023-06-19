while True:
    num1, num2 = input("Escribe dos números separados por espacio: ").split()
    sign = input("Ingrese signo: ")

    if len(sign) > 0:
        if num1.isnumeric() and num2.isnumeric():
            int_num1 = int(num1)
            int_num2 = int(num2)
            if sign == "+":
                print(
                    f"La suma de {num1} y {num2} "
                    f"es igual a {int_num1 + int_num2}"
                )
            elif sign == "-":
                print(
                    f"La resta de {num1} y {num2} "
                    f"es igual a {int_num1 - int_num2}"
                )
            elif sign == "*":
                print(
                    f"La multiplicación de {num1} y {num2} "
                    f"es igual a {int_num1 * int_num2}"
                )
            elif sign == "/":
                print(
                    f"La división de {num1} y {num2} "
                    f"es igual a {int_num1 / int_num2}"
                )
            else:
                print("El signo no es el correcto!")
        else:
            print("Los números deben ser valores calculables!")
    else:
        print("El signo no puede ser vacío!")

    ask = input("Desea continuar? (s/n): ")

    if ask == "n" or ask == "no":
        print("Gracias por utilizar la Calculadora v2.0")
        break
