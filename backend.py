import random
import settings
from card_templates import template as template_deck, Сard


class Status:
    class Win:
        pass

    class Overdo:
        pass

    class DealerMinimum:
        pass

    class FullLose:
        pass

    class Playing:
        pass

    class DealerPlaying:
        pass

    class DealerStop:
        pass


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

    def __del__(self):
        self.__isInstance = False


class Hand:
    def __init__(self):
        self._cards: list = []
        self._score: int = 0

    def __add__(self, other):
        if not isinstance(other, Сard):
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

    def _calculate_score(self):
        arr_value = []
        score = 0
        for card in self.cards:
            arr_value.append(card.value)
        arr_value.sort()

        for value in arr_value:
            if value == 11 and (self._score + 11) > 21:
                score += 1
            else:
                score += value

        return score

    def clean(self):
        self._cards = []


class Table:
    def __init__(self, player: Player):
        self.player = player
        self.deck = Deck()
        self.dealer = Dealer()
        self.hand_dealer = None

    def clear_hands(self):
        self.player.hand.clean()
        self.dealer.hand.clean()

    def get_score_player(self):
        return self.player.hand.score

    def get_score_dealer(self):
        return self.hand_dealer.value

    def check_21_player(self):
        return self.player.hand == 21

    def check_player_balance(self):
        return self.player.bank > 0

    def deal_cards(self):
        self.dealer.hand += self.deck.get_card()
        for _ in range(settings.STARTED_COUNT_CARD_IN_PLAYER_HAND):
            self.player.hand += self.deck.get_card()

    def add_card_player(self):
        self.player.hand += self.deck.get_card()
        return self.player.hand.status

    def check_break(self):
        return self.player.hand > 21

    def check_break_dealer(self):
        return self.get_score_dealer() > 21

    def check_score_dealer(self):
        return self.get_score_dealer() < 17

    def add_card_dealer(self):
        self.dealer.hand += self.deck.get_card()


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
