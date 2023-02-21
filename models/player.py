from models.status import Status
from models.hand import Hand


class Player:

    def __init__(self, bank):
        self._bet = None
        self._bank = bank
        self._hand = Hand()

    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, value):
        if not isinstance(value, int):
            raise TypeError('Неверный тип')
        if value < 0:
            raise ValueError('Отрицательное значение')
        if value > self.bank:
            raise ValueError('Ставка не может привышать размер банка')

        self._bet = value

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        if isinstance(value, Hand):
            self._hand = value
        else:
            raise TypeError('В руку можно положить только карты')

    @property
    def status(self):
        if self._bank <= 0:
            return Status.FullLose
        else:
            return Status.Playing

    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, value):
        if not isinstance(value, int):
            raise TypeError('Неверный формат')
        self._bank = value

    def win(self):
        self.bank += self.bet

    def lose(self):
        self.bank -= self.bet
        if not self._bank > 0:
            return Status.FullLose
        else:
            return Status.Playing
