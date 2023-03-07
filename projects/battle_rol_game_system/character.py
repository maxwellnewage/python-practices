class Character:
    def __init__(self, name, hp, atq, df):
        self.name = name
        self.hp = hp
        self.atq = atq
        self.df = df

    def __str__(self):
        return f"Character: {self.name}"

    def attack(self, target):
        damage = max(self.atq - target.df, 0)
        target.hp -= damage
        print(f"{self.name} ha causado {damage} puntos de daño a {target.name}.")

    def is_alive(self):
        return self.hp > 0
