from character import Character
from random import choice, randint


class Enemy(Character):
    type_list = ['goblin', 'orco', 'troll', 'araña']
    name_list = ['Waldorf', 'Aracdic', 'Wallos', 'Mordorux']

    def __init__(self):
        enemy_type = choice(self.type_list)
        enemy_name = choice(self.name_list)
        hp = randint(10, 20)
        atq = randint(5, 10)
        df = randint(1, 5)
        self.enemy_type = enemy_type
        super().__init__(enemy_name, hp, atq, df)

    def __str__(self):
        return f"Enemigo {self.enemy_type}: {self.name} (HP: {self.hp})"
