import settings
from models.status import Status
from models.card import Card, template


class Hand:
    def __init__(self):
        self._cards: list = []

    def __add__(self, other):
        if not isinstance(other, Card):
            raise TypeError('Класть в руку можно только карты')

        if not other in template:
            raise ValueError('Карта явно не из той колоды')

        self._cards.append(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return f'{self._cards} score: {self.score}'

    @staticmethod
    def _check_type_compare(other):
        if not isinstance(other, int):
            raise TypeError('Сравнивать можно только значение score с int значением')

    @property
    def cards(self):
        return self._cards

    @property
    def status(self):
        if self.score > settings.BLACK_JACK:
            return Status.Overdo
        if self.score == settings.BLACK_JACK:
            return Status.Win
        if self.score >= settings.DEALER_SCORE_STOP:
            return Status.DealerStop
        else:
            return Status.DealerPlaying


    @property
    def score(self):
        return self._calculate_score()

    def _get_sort_value_cards(self):
        return sorted(card.value for card in self.cards)

    def _calculate_score(self):
        score = 0
        for value in self._get_sort_value_cards():
            if value == 11 and (score + 11) > 21:
                score += 1
            else:
                score += value

        return score

    def clean(self):
        self._cards = []
