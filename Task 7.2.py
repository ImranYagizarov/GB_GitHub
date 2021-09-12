# Part 7.2 (Materials calculation)

from abc import ABC, abstractmethod

class Clothes(ABC):  # Основной класс

    @abstractmethod
    def material(self):
        pass

    # def summary_material(self, c, s):
    #     self.c = c
    #     self.s = s
    #     result = self.c + self.s
    #     return result


class Coat(Clothes):  # Дочерний класс

    def __init__(self, v):
        self.v = v

    @property
    def material(self):
        result = self.v / 6.5 + 0.5
        return result


class Suit(Clothes):  # Дочерний класс

    def __init__(self, h):
        self.h = h

    @property
    def material(self):
        result = 2 * self.h + 0.3
        return result


coat = Coat(4)
suit = Suit(6)
#clothes = Clothes.summary_material(4, 6) ???
print(coat.material)
print(suit.material)
print(clothes)

