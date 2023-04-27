from calculadora import Calculadora

while True:
    try:
        num1, num2 = input("Escribe dos números separados por espacio: ").split()
        sign = input("Ingrese signo: ")

        calc = Calculadora(num1, num2, sign)

        ask = input("Desea continuar? (s/n/h/u): ")

        if ask == "u":
            calc.view_op_history_last()
        elif ask == "h":
            calc.view_op_history()
        elif ask == "n" or ask == "no":
            calc.bye()
            break
    except ValueError:
        print("La cantidad de valores no son correctas, por favor reintentar!")
