from dataclasses import dataclass


@dataclass(frozen=True)
class Сard:
    name: str
    value: int


template = [
    Сard(name='A', value=11),
    Сard(name='2', value=2),
    Сard(name='3', value=3),
    Сard(name='4', value=4),
    Сard(name='5', value=5),
    Сard(name='6', value=6),
    Сard(name='7', value=7),
    Сard(name='8', value=8),
    Сard(name='9', value=9),
    Сard(name='10', value=10),
    Сard(name='J', value=10),
    Сard(name='D', value=10),
    Сard(name='K', value=10),
]


class Hand:
    def __init__(self):
        self.__cards: list = []
        self.__value: int = 0

    def __add__(self, other):
        if isinstance(other, Сard):
            self.cards.append(other)
            self.__calculate_score()
        else:
            raise TypeError('Класть в руку можно только карты')
        return self

    def __str__(self):
        return f'{self.cards} score: {self.value}'

    @property
    def cards(self):
        return self.__cards

    @property
    def value(self):
        return self.__value

    def __calculate_score(self):
        arr_value = []
        for card in self.cards:
            arr_value.append(card.value)
        arr_value.sort()

        for value in arr_value:
            if value == 11 and (self.value + 11) > 21:
                self.__value += 1
            else:
                self.__value += value

