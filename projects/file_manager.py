"""
Explorador de archivos.
"""

import os
import shutil

# Nuestro source es la carpeta del proyecto, entonces vamos un nivel hacia arriba
source = "../"

py_file_formats = ['py']
project_file_formats = ['git', 'idea', 'md']

files = os.listdir(source)
py_file_list = []
project_file_list = []

for file in files:
    file_ext = file.split('.')[-1]

    if file_ext in py_file_formats:
        py_file_list.append(file)
    elif file_ext in project_file_formats:
        project_file_list.append(file)

for index, py_file in enumerate(py_file_list):
    if index == 0:
        print("-- Archivos de Python --")
    print(py_file)

for index, project_file in enumerate(project_file_list):
    if index == 0:
        print("-- Archivos de Proyecto --")
    print(project_file)

