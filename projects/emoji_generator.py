import random


class EmojiGenerator:
    def __init__(self):
        self.__emojis = ["😂", "😅", "🚀", "🎮", "🐍", "🍾", "👌", "💰"]

    def get_emojis(self):
        # random.shuffle(self.__emojis)
        return self.__emojis

    def get_emoji(self):
        return random.choice(self.__emojis)

    def insert_emoji(self, emoji):
        if emoji:
            self.__emojis.append(emoji)


if __name__ == '__main__':
    emoji_gen = EmojiGenerator()

    emoji_gen.insert_emoji("🚽")

    print(emoji_gen.get_emojis())
