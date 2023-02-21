import settings
from models.card import template as template_deck
import random


class Deck:
    __isInstance = False

    def __init__(self):
        self.__create_deck()

    def __new__(cls, *args, **kwargs):
        if not cls.__isInstance:
            cls.__isInstance = super().__new__(cls)
        return cls.__isInstance

    def __del__(self):
        self.__isInstance = False

    def __str__(self):
        return f'Count card:{len(self.__cards)}'

    def get_card(self):
        if len(self.__cards) < (settings.COUNT_CARD_IN_NORM_DECK * settings.COUNT_DECKS / 2):
            self.__create_deck()
        return self.__cards.pop(0)

    def __create_deck(self):
        cards = []
        for card in template_deck:
            for _ in range(settings.COUNT_DECKS * 4):
                cards.append(card)
        random.shuffle(cards)
        self.__cards = cards
