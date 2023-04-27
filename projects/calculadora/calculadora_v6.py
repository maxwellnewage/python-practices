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
    write_history_file(op)
    print(op)


def view_op_history_last():
    print("-----Historial de las últimas 3 Operaciones-----")
    for i, operation in enumerate(operation_history):
        if (i + 1) > 3:
            break

        print(f"{i + 1}. {operation}")


def view_op_history():
    with open("history.txt", "r") as history_file:
        history_list = history_file.readlines()
        for i, h in enumerate(history_list):
            if i == 0:
                print(h.strip())
                continue

            print(f"{i}. {h.strip()}")


def bye():
    print("Gracias por utilizar la Calculadora v6.0")


def write_history_file(op_history: str):
    with open("history.txt", "a") as history_file:
        history_file.write("\n" + op_history)


operation_history = []

while True:
    try:
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
    except ValueError:
        print("La cantidad de valores no son correctas, por favor reintentar!")

    ask = input("Desea continuar? (s/n/h/u): ")

    if ask == "u":
        view_op_history_last()
    elif ask == "h":
        view_op_history()
    elif ask == "n" or ask == "no":
        bye()
        break
