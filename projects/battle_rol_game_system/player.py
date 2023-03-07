from character import Character


class Player(Character):
    def __init__(self, name):
        super().__init__(name, 20, 5, 3)

    def __str__(self):
        return f"{self.name} tu HP es {self.hp}"
