import settings
from models.status import Status
from models.card import Card


class Hand:
    def __init__(self):
        self._cards: list = []
        self._score: int = 0

    def __add__(self, other):
        if not isinstance(other, Card):
            raise TypeError('Класть в руку можно только карты')
        self._cards.append(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return f'{self._cards} score: {self.score}'

    def __eq__(self, other):
        self._check_type_compare(other)
        return self.score == other

    def __ne__(self, other):
        self._check_type_compare(other)
        return self.score != other

    def __lt__(self, other):
        self._check_type_compare(other)
        return self.score < other

    def __le__(self, other):
        self._check_type_compare(other)
        return self.score <= other

    def __gt__(self, other):
        self._check_type_compare(other)
        return self.score > other

    def __ge__(self, other):
        self._check_type_compare(other)
        return self.score >= other

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
        if self.score < settings.DEALER_SCORE_STOP:
            return Status.DealerPlaying
        if self.score > settings.DEALER_SCORE_STOP:
            return Status.DealerStop

    @property
    def score(self):
        return self._calculate_score()

    def _get_value_cards(self):
        return sorted(card.value for card in self.cards)

    def _calculate_score(self):
        score = 0
        for value in self._get_value_cards():
            if value == 11 and (self._score + 11) > 21:
                score += 1
            else:
                score += value

        return score

    def clean(self):
        self._cards = []
