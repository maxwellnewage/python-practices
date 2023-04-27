def operate(op_word, n1, n2):
    op = ""
    int_n1 = int(n1)
    int_n2 = int(n2)

    if op_word == "suma":
        op = f"La {op_word} de {n1} y {n2} es igual a {int_n1 + int_n2}"
    elif op_word == "resta":
        op = f"La {op_word} de {n1} y {n2} es igual a {int_n1 - int_n2}"
    elif op_word == "multiplicación":
        op = f"La {op_word} de {n1} y {n2} es igual a {int_n1 * int_n2}"
    elif op_word == "división":
        op = f"La {op_word} de {n1} y {n2} es igual a {int_n1 / int_n2}"

    operation_history.append(op)
    print(op)


def view_op_history():
    print("-----Historial de Operaciones-----")
    for i, operation in enumerate(operation_history):
        print(f"{i + 1}. {operation}")


def bye():
    print("Gracias por utilizar la Calculadora v4.0")


operation_history = []

while True:
    num1, num2 = input("Escribe dos números separados por espacio: ").split()
    sign = input("Ingrese signo: ")

    if len(sign) > 0:
        if num1.isnumeric() and num2.isnumeric():
            if sign == "+":
                operate("suma", num1, num2)
            elif sign == "-":
                operate("resta", num1, num2)
            elif sign == "*":
                operate("multiplicación", num1, num2)
            elif sign == "/":
                operate("división", num1, num2)
            else:
                print("El signo no es el correcto!")
        else:
            print("Los números deben ser valores calculables!")
    else:
        print("El signo no puede ser vacío!")

    ask = input("Desea continuar? (s/n/h): ")

    if ask == "h":
        view_op_history()
    elif ask == "n" or ask == "no":
        bye()
        break
