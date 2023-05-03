"""
Devolver todos los números de teléfono de una cadena
"""
import re


def find_all_phone_numbers(text):
    phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    return phone_regex.findall(text)


if __name__ == '__main__':
    print(find_all_phone_numbers("""
        Esto es un numero de télefono: 415-232-2333, 
        esto no 444-222, 
        pero esto si 445-252-2333
    """))
