class Calculadora:
    operation_history = []
    VERSION = "7.0"

    def __init__(self, n1, n2, sign):
        self.n1 = n1
        self.n2 = n2
        self.sign = sign
        self.__detect_operator()

    def both_numeric(self):
        return self.n1.isnumeric() and self.n2.isnumeric()

    def sign_not_empty(self):
        return len(self.sign) > 0

    def __detect_operator(self):
        if self.sign_not_empty():
            if self.both_numeric():
                if self.sign == "+":
                    self.__operate("suma")
                elif self.sign == "-":
                    self.__operate("resta")
                elif self.sign == "*":
                    self.__operate("multiplicación")
                elif self.sign == "/":
                    self.__operate("división")
                else:
                    print("El signo no es el correcto!")
            else:
                print("Los números deben ser valores calculables!")
        else:
            print("El signo no puede ser vacío!")

    def __operate(self, op_word):
        op = ""
        int_n1 = int(self.n1)
        int_n2 = int(self.n2)

        if op_word == "suma":
            op = f"La {op_word} de {self.n1} y {self.n2} es igual a {int_n1 + int_n2}"
        elif op_word == "resta":
            op = f"La {op_word} de {self.n1} y {self.n2} es igual a {int_n1 - int_n2}"
        elif op_word == "multiplicación":
            op = f"La {op_word} de {self.n1} y {self.n2} es igual a {int_n1 * int_n2}"
        elif op_word == "división":
            op = f"La {op_word} de {self.n1} y {self.n2} es igual a {int_n1 / int_n2}"

        self.operation_history.append(op)
        self.__write_history_file(op)
        print(op)

    def __write_history_file(self, op_history: str):
        with open("history.txt", "a") as history_file:
            history_file.write("\n" + op_history)

    def view_op_history_last(self):
        print("-----Historial de las últimas 3 Operaciones-----")
        for i, operation in enumerate(self.operation_history):
            if (i + 1) > 3:
                break

            print(f"{i + 1}. {operation}")

    def view_op_history(self):
        with open("history.txt", "r") as history_file:
            history_list = history_file.readlines()
            for i, h in enumerate(history_list):
                if i == 0:
                    print(h.strip())
                    continue

                print(f"{i}. {h.strip()}")

    def bye(self):
        print(f"Gracias por utilizar la Calculadora v{self.VERSION}")
