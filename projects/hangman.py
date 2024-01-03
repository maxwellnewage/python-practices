import random


def get_word_lines(word):
    guess_word = []

    for _ in chosen_word:
        guess_word.append("_")

    return guess_word


if __name__ == '__main__':
    word_list = ["car", "cat", "boy", "girl", "address", "member"]
    chosen_word = random.choice(word_list)
    guess_word = get_word_lines(chosen_word)
    guessed = False
    lives = len(guess_word) + 2

    print(guess_word)

    while not guessed:
        print(f"Lives: {lives}")

        guess = input("Guess a letter: ").lower()
        match = False

        for i, letter in enumerate(chosen_word):
            if guess == letter:
                print("Good choice!")
                guess_word[i] = letter
                match = True

        print(guess_word)

        if not match:
            lives -= 1
            print(f"Wrong!")

        if lives <= 0:
            print("You lose...")
            break

        if "_" not in guess_word:
            guessed = True
            print("You Win!")
