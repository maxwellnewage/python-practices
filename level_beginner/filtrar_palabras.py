"""
Escribir una función filtrar_palabras()
que tome una lista de palabras y un entero n,
y devuelva las palabras que tengan más de n caracteres.
"""


def filtrar_palabras(words_list: list[str], chars: int):
    words_more_n_chars = []
    for w in words_list:
        if len(w) > chars:
            words_more_n_chars.append(w)
    return words_more_n_chars


if __name__ == '__main__':
    print(filtrar_palabras(["lista", "de", "palabras"], 2))
    print(filtrar_palabras(["aaa", "b", "cc"], 2))
    print(filtrar_palabras(["a", "bb", "ccc", "dddd"], 3))
