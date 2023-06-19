"""
Crear un teléfono inteligente que posea distintas características
aplicadas con herencia múltiple.
"""


class Phone:
    def __init__(self):
        pass

    def call(self):
        print("Calling...")

    def busy(self):
        print("Is busy...")


class Camera:
    def __init__(self):
        pass

    def take_picture(self):
        print("Taking a picture!")


class Player:
    def __init__(self):
        pass

    def play_song(self):
        print("Playing a song...")


class SmartPhone(Phone, Camera, Player):
    pass


if __name__ == '__main__':
    smartphone = SmartPhone()
    smartphone.call()
    smartphone.play_song()
    smartphone.take_picture()
