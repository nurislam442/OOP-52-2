import random
from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.__random_int = random.randint(1, 3)

    def get_random_int(self):
        return self.__random_int

    def attack(self):
        print(f"{self.name} наносит удар!")

    def protection(self):
        print(f"{self.name} защищается!")

    def rest(self):
        print(f"{self.name} отдыхает и восстанавливает силы!")

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass
