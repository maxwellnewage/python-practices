"""
Calcula el amor ideal según el nombre de las personas
https://www.udemy.com/course/100-days-of-code/learn/lecture/17965130
"""


def count_letters(letters, names):
    letter_count = 0
    for letter in letters:
        letter_count += names.count(letter)

    return letter_count


def true_love_score(true, love):
    return int(str(true) + str(love))


def get_score_msg(love_score):
    if love_score < 10 or love_score > 90:
        print(f"Love score is nice! ({love_score})")
    elif 40 <= love_score <= 50:
        print(f"Love score is alright ({love_score})")
    else:
        print(f"Love score is very low... ({love_score})")


if __name__ == '__main__':
    print("-"*30)
    print("Bienvenidos a Love Calculator!")
    your_name = input("Escribe tu nombre: ").lower()
    their_name = input("Escribe su nombre: ").lower()

    names = your_name + their_name

    true_counter = count_letters("true", names)
    love_counter = count_letters("love", names)

    tl_score = true_love_score(true_counter, love_counter)

    get_score_msg(tl_score)
