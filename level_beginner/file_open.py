"""
Crear un archivo y escribir algo dentro seguido de salto de linea.
Luego leer la información acumulada

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""

FILE = "resources/generated/file_open.txt"

file_append = open(FILE, "a")
file_append.write(input("Escribe algo: ") + "\n")
file_append.close()

file_read = open(FILE, "r")
print(file_read.read())
