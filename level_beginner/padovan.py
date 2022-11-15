"""
Padovan numbers
https://www.codewars.com/kata/5803ee0ed5438edcc9000087/train/python
"""


def padovan(n):
    if n <= 2:
        return 1
    else:
        return padovan(n - 2) + padovan(n - 3)


pad_list = []
for num in range(15):
    pad_list.append(padovan(num))
print(pad_list)
