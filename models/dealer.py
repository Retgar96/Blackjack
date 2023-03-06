from models.hand import Hand


class Dealer:

    def __init__(self):
        self._hand = Hand()

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        self._hand = value

    def __add__(self, other):
        return self.hand + other

    def __iadd__(self, other):
        return self.__add__(other)

