"""
Escribir una función mas_larga()
que tome una lista de palabras y devuelva la mas larga.
"""


def clean_signs(phrase):
    signs = ["¿", "?", "¡", "!", ".", ","]
    for s in signs:
        phrase = phrase.replace(s, "")
    return phrase


def mas_larga(phrase):
    phrase = clean_signs(phrase)
    words = phrase.split()
    largest_word = words[0]
    for w in words:
        if w > largest_word:
            largest_word = w
    return largest_word


if __name__ == '__main__':
    print(mas_larga("¿Cual es la palabra mas larga?"))
    print(mas_larga("Si la palabra es palindromo, esta bien"))
    print(mas_larga("Esto es una gran frase"))
