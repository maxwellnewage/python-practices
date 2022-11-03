from abc import abstractmethod


class Movement:
    @abstractmethod
    def move_up(self):
        pass

    @abstractmethod
    def move_down(self):
        pass

    @abstractmethod
    def move_left(self):
        pass

    @abstractmethod
    def move_right(self):
        pass
