from models.status import Status
from models.hand import Hand


class Bet:

    def __get__(self, instance, owner):
        return instance.value

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Неверный тип')
        if value < 0:
            raise ValueError('Отрицательное значение')
        if value > instance.bank:
            raise ValueError('Ставка не может привышать размер банка')
        instance.value = value


class Player:
    bet = Bet()
    hand = Hand()

    def __init__(self, bank):
        if not isinstance(bank, int):
            raise TypeError()
        if bank < 1:
            raise ValueError('Банк не может быть отритцательным')
        self._bank = bank

    @property
    def status(self):
        if self._bank <= 0:
            return Status.FullLose
        else:
            return Status.Playing

    @property
    def bank(self):
        return self._bank

    def win(self):
        self._bank += self.bet

    def lose(self):
        self._bank -= self.bet
        if not self._bank > 0:
            return Status.FullLose
        else:
            return Status.Playing
