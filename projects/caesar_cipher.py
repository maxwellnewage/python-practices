alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, direction):
    final_text = ""
    for char in plain_text:
        if char in alphabet:
            if direction == "e":
                index = alphabet.index(char) + shift_amount
            else:
                index = alphabet.index(char) - shift_amount

            final_text += alphabet[index]
        else:
            final_text += char
    return final_text


while True:
    direction = input("Type '(e)ncode' to encrypt, type '(d)ecode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    print(caesar(text, shift, direction))

    keep = input("Continue? (y/n): ").lower()
    if keep == "n":
        break


