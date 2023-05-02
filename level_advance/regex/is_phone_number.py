"""
Devolver un booleano según la validez del número de teléfono
"""
import re


# check Canada Phone like 415-555-4444 (no regex)
def is_phone_number(text):
    if len(text) != 12:
        return False  # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # no area code
    if text[3] != '-':
        return False  # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # no first 3 digits
    if text[7] != '-':
        return False  # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # missing last 4 digits
    return True


def is_phone_number_regex(text):
    phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phone_regex.search(text)
    return mo is not None


print(is_phone_number('415-232-2333'), is_phone_number('415-232-333'))
print(is_phone_number_regex('415-232-2333'), is_phone_number_regex('415-232-333'))
