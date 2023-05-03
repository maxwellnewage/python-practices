"""
Devolver el número de teléfono encontrado por grupos
"""
import re


def phone_number_group(text):
    phone_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    return phone_regex.search(text)


if __name__ == '__main__':
    phone_group = phone_number_group('415-232-2333')
    print(phone_group.group(1))
    print(phone_group.group(2))
