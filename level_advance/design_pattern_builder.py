"""
Aplicación del Patron de diseño Builder
"""


class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.money = 10
        self.attack = 0
        self.defense = 0

    def __str__(self):
        return \
            f"Hero: {self.name} | " \
            f"💰{self.money} ⚔{self.attack} 🛡{self.defense}"


class HeroBuilder:
    def __init__(self, name):
        self.hero = Hero(name)

    def set_attack(self, attack):
        # si me envían un ataque inferior al actual,
        # preservo el que ya tenía
        self.hero.attack = max(attack, self.hero.attack)
        return self

    def set_defense(self, defense):
        # si me envían una defensa inferior a la actual,
        # preservo la que ya tenía
        self.hero.defense = max(defense, self.hero.defense)
        return self

    def add_money(self, money):
        self.hero.money += max(money, 0)
        return self

    def get_hero(self):
        return self.hero


if __name__ == '__main__':
    builder = HeroBuilder("Tomas")
    builder.set_attack(-5).set_defense(10)
    builder.add_money(10).add_money(20).add_money(30)
    hero = builder.get_hero()

    print(hero)
