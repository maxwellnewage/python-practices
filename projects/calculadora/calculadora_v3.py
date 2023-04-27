operation_history = []

while True:
    num1, num2 = input("Escribe dos números separados por espacio: ").split()
    sign = input("Ingrese signo: ")

    if len(sign) > 0:
        if num1.isnumeric() and num2.isnumeric():
            int_num1 = int(num1)
            int_num2 = int(num2)
            if sign == "+":
                operation = f"La suma de {num1} y {num2} es igual a {int_num1 + int_num2}"
                operation_history.append(operation)
                print(operation)
            elif sign == "-":
                operation = f"La resta de {num1} y {num2} es igual a {int_num1 - int_num2}"
                operation_history.append(operation)
                print(operation)
            elif sign == "*":
                operation = f"La multiplicación de {num1} y {num2} es igual a {int_num1 * int_num2}"
                operation_history.append(operation)
                print(operation)
            elif sign == "/":
                operation = f"La división de {num1} y {num2} es igual a {int_num1 / int_num2}"
                operation_history.append(operation)
                print(operation)
            else:
                print("El signo no es el correcto!")
        else:
            print("Los números deben ser valores calculables!")
    else:
        print("El signo no puede ser vacío!")

    ask = input("Desea continuar? (s/n/h): ")

    if ask == "h":
        print("-----Historial de Operaciones-----")
        for i, operation in enumerate(operation_history):
            print(f"{i + 1}. {operation}")
    elif ask == "n" or ask == "no":
        print("Gracias por utilizar la Calculadora v3.0")
        break
