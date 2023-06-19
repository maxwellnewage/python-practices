from player import Player
from enemy import Enemy


class Game:
    def __init__(self):
        self.player = None
        self.enemy = None

    def start(self):
        print("Bienvenido a Battle of Deponia!")
        player_name = input("Introduce tu nombre: ")
        print(f"Hola, {player_name}")
        self.player = Player(player_name)
        self.enemy = Enemy()
        print(f"Te encuentras con {self.enemy}.")
        self.start_combat()

    def start_combat(self):
        while self.player.is_alive() and self.enemy.is_alive():
            # Turno del jugador
            print(self.player)
            print(self.enemy)

            action = input("Qué deseas hacer? [atq/huir]: ")

            if action == "atq":
                self.player.attack(self.enemy)
            elif action == "huir":
                print("Te has escapado del combate!")
            else:
                print("Acción no válida!")
                continue

            # Turno del enemigo
            if self.enemy.is_alive():
                self.enemy.attack(self.player)

        if self.player.is_alive():
            print(
                f"Felicidades {self.player.name}, "
                f"has vencido a {self.enemy.name}!"
            )
        else:
            print(f"Has sido derrotado por {self.enemy.name}...")
