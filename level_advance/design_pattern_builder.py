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
        return f"Hero: {self.name} | 💰{self.money} ⚔{self.attack} 🛡{self.defense}"


class HeroBuilder:
    def __init__(self, name):
        self.hero = Hero(name)

    def set_attack(self, attack):
        if attack > 0:
            self.hero.attack = attack
        return self

    def set_defense(self, defense):
        if defense > 0:
            self.hero.defense = defense
        return self

    def add_money(self, money):
        self.hero.money += max(money, 0)  # evito dinero negativo
        return self

    def get_hero(self):
        return self.hero


builder = HeroBuilder("Tomas")
builder.set_attack(5).set_defense(10)
builder.add_money(10).add_money(20).add_money(30)
hero = builder.get_hero()

print(hero)
