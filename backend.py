import random

from exceptions import BetExcessException, BetNegative
import settings
from card_templates import template as template_deck


class GameTable:

    def __init__(self):
        self.deck = Deck()
        self.bank = None
        self.bet = None
        self.dealer_card = []
        self.player_card = []

    def clear_hands(self):
        self.dealer_card = []
        self.player_card = []

    def get_score_player(self):
        return self.calculate_score(self.player_card)

    def get_score_dealer(self):
        return self.calculate_score(self.dealer_card)

    def check_21_player(self):
        return self.calculate_score(self.player_card) == 21

    def add_bet(self):
        self.bank += self.bet

    def minus_bet(self):
        self.bank -= self.bet

    def check_balance(self):
        return self.bank > 0

    def check_bet(self):
        if self.bet > self.bank:
            raise BetExcessException
        elif self.bet < 1:
            raise BetNegative

    def deal_cards(self):
        self.dealer_card.append(self.deck.get_card())
        for _ in range(settings.STARTED_COUNT_CARD_IN_PLAYER_HAND):
            self.player_card.append(self.deck.get_card())

    def add_card_player(self):
        self.player_card.append(self.deck.get_card())

    def check_break_player(self):
        return self.get_score_player() > 21

    def check_break_dealer(self):
        return self.get_score_dealer() > 21

    def check_score_dealer(self):
        return self.get_score_dealer() < 17

    def add_card_dealer(self):
        self.dealer_card.append(self.deck.get_card())

    @staticmethod
    def calculate_score(cards):
        result = 0
        hand_value = []
        for card in cards:
            hand_value.append(card.value)
        hand_value.sort()

        for value in hand_value:
            if value == 11 and (result + 11) > 21:
                result += 1
            else:
                result += value

        return result


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
        if len(self.__cards) < (settings.COUNT_CARD_IN_STANDART_DECK * settings.COUNT_DECKS / 2):
            self.__create_deck()
        return self.__cards.pop(0)

    def __create_deck(self):
        cards = []
        for card in template_deck:
            for _ in range(settings.COUNT_DECKS * 4):
                cards.append(card)
        random.shuffle(cards)
        self.__cards = cards



