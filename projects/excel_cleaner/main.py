import re
import openpyxl

# Abre el archivo Excel existente
workbook = openpyxl.load_workbook('file_input.xlsx')

# Selecciona la hoja de trabajo en la que se trabajará
worksheet = workbook['Hoja1']

for row in worksheet.iter_rows():
    for cell in row:
        # Realiza una operación en cada celda
        if cell.value is not None and isinstance(cell.value, str):
            cell.value = re.sub(r'\s+', ' ', cell.value)

# Guarda los cambios sin modificar los estilos
workbook.save('file_output.xlsx')
