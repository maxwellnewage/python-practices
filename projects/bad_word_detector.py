"""
Lee una frase de la consola y la censura.
"""

# lista de palabras censuradas
deny_words = ["manzana", "pera", "pomelo", "cacao", "avenida"]


# recibo un string de frase y retorno otro string convertido
def phrase_filter(phrase: str) -> str:
    # separo la frase en palabras: split() = split(" ")
    words = phrase.split()
    final_words = ""
    # utilizo enumerate para tener index y evitar el espacio al principio del string
    for index, word in enumerate(words):
        if word in deny_words:
            final_words += " [censurado]"
        else:
            final_words += word if index == 0 else f" {word}"
    return final_words


print(phrase_filter("Me gusta la manzana porque se parece a una avenida"))
