import random
from abc import ABC, abstractmethod

import card_templates
from exceptions import BetExcessException, BetNegative
import settings
from card_templates import template as template_deck, Сard


# class Table(ABC):
#     players = []
#     dealer = '_dealer'
#     deck = '_deck'
#
#     @abstractmethod
#     def qewe(self):
#         pass
#
#
# class Dealer:
#     minimum_score = 17
#     hand = '_Hand'
#
#
#
#
# class Round:
#     table = '_Table'
#     dealer = '_Dealer'
#     players = '[]_Player'


class Player:
    def __new__(cls, bank):
        if bank < 0 or type(bank) not in ('int', 'float'):
            raise TypeError('Неверный формат')
        return super(Player, cls).__new__(cls)

    def __init__(self, bank):
        self._bank = bank
        self.hand = Hand()
        self.bet = None

    @property
    def bank(self):
        return self._bank

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self._bank += float
        elif isinstance(other, card_templates.Сard):
            self.hand = self.hand + other
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            if self._bank < other:
                True
            else:
                return False
        elif isinstance(other, Hand):
            if self.hand.value < other.value:
                return True
            else:
                return False
        return self

    def __gt__(self, other):
        self.__lt__(other)

    def __setattr__(self, name, value):
        if name == 'bet':
            if not isinstance(value, int or float) or value > 0:
                raise Exception.BetExceptions
            if value > self._bank:
                raise BetExcessException
            super.__setattr__(self, name, value)

    def win(self):
        self._bank += self.bet

    def lose(self):
        self._bank -= self.bet
        if not self._bank > 0:
            raise Exception.PlayerLose('Игрок проиграл')


class Dealer(Player):
    __isInstance = False

    def __del__(self):
        self.__isInstance = False

    def __new__(cls, *args, **kwargs):
        if not cls.__isInstance:
            cls.__isInstance = super().__new__(cls)
        return cls.__isInstance

    def


class Hand:
    def __init__(self):
        self.__cards: list = None
        self.__value: int = None

    def __add__(self, other):
        if isinstance(other, Сard):
            self.__cards.append(other)
            self.__calculate_score()
        else:
            raise TypeError('Класть в руку можно только карты')
        return self

    def __len__(self):
        return len(self.__cards)

    def __str__(self):
        return f'{self.__cards} score: {self.__value}'

    @property
    def cards(self):
        return self.__cards

    @property
    def value(self):
        return self.__calculate_score()

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

        return self.__value

    def clean(self):
        self.__cards = None
        self.__value = None


# class Score:
#     @staticmethod
#     def calculate_score(cards):
#         result = 0
#         hand_value = []
#         for card in cards:
#             hand_value.append(card.value)
#         hand_value.sort()
#
#         for value in hand_value:
#             if value == 11 and (result + 11) > 21:
#                 result += 1
#             else:
#                 result += value
#
#         return result


class Table:
    __isInstance = False

    def __del__(self):
        self.__isInstance = False

    def __new__(cls, *args, **kwargs):
        if not cls.__isInstance:
            cls.__isInstance = super().__new__(cls)
        return cls.__isInstance

    def __init__(self, player: Player):
        self.player = player
        self.deck = Deck()
        # self.bank = None
        # self.bet = None
        self.hand_dealer = None
        # self.hand_player = []

    def clear_hands(self):
        self.hand_dealer = None
        # self.hand_player = []
        self.player.hand.clean()

    def get_score_player(self):
        return self.player.hand.value

    def get_score_dealer(self):
        return self.hand_dealer.value

    def check_21_player(self):
        return self.player.hand == 21

    # def add_bet(self):
    #     self.player.win()

    # def minus_bet(self):
    #     self.player.lose()

    def check_balance(self):
        return self.player > 0

    def check_bet(self):
        if self.bet > self.bank:
            raise BetExcessException
        elif self.bet < 1:
            raise BetNegative

    def deal_cards(self):
        self.hand_dealer.append(self.deck.get_card())
        for _ in range(settings.STARTED_COUNT_CARD_IN_PLAYER_HAND):
            self.player.hand + self.deck.get_card()

    def add_card_player(self):
        self.player.hand + self.deck.get_card()

    def check_break(self, player):
        return player > 21

    def check_break_dealer(self):
        return self.get_score_dealer() > 21

    def check_score_dealer(self):
        return self.get_score_dealer() < 17

    def add_card_dealer(self):
        self.hand_dealer.append(self.deck.get_card())

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
