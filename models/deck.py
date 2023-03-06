import settings
from models.card import template as template_deck
import random


class Deck:
    def __init__(self):
        self._cards = []
        self._create_deck()

    def __str__(self):
        return f'Count card:{len(self._cards)}'

    def __len__(self):
        return len(self._cards)

    def get_card(self):
        if len(self._cards) < (settings.COUNT_CARD_IN_NORM_DECK * settings.COUNT_DECKS / 2):
            self._create_deck()
        return self._cards.pop(0)

    def _create_deck(self):
        cards = []
        for card in template_deck:
            for _ in range(settings.COUNT_DECKS * 4):
                cards.append(card)
        random.shuffle(cards)
        self._cards = cards
