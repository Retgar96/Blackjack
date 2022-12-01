import random
import settings
from card_templates import template as temlate_deck


class GameTable:

    def __init__(self):
        self.deck = Deck()
        self.bank = None
        self.bet = None
        self.dealer_card = ''
        self.player_card = ''

    def get_score_player(self):
        return self.__calculate_score(self.player_card)

    def get_score_dealer(self):
        return self.__calculate_score(self.dealer_card)

    def check_21_player(self):
        return self.__calculate_score(self.player_card) == 21

    def add_bet(self):
        self.bank += self.bet

    def minus_bet(self):
        self.bank -= self.bet

    def check_balance(self):
        return self.bank > 0

    def check_bet(self):
        return self.bet <= self.bank

    def create_deck(self):
        self.deck = Deck()

    def deal_cards(self):
        self.dealer_card = [self.deck.get_card()]
        self.player_card = [self.deck.get_card() for i in range(settings.STARTED_COUNT_CARD_IN_PLAYER_HAND)]
        return

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

    # @staticmethod
    # def __calculate_score(cards):
    #     result = 0
    #     for card in cards:
    #         if card['name'] == 'T' and (result + 11) > 21:
    #             result = result + 1
    #         else:
    #             result = result + card['value']
    #     return result
    @staticmethod
    def __calculate_score(cards):
        result = 0
        hand_value = []
        for card in cards:
            hand_value.append(card['value'])
        hand_value.sort()

        for value in hand_value:
            if value == 11 and (result + 11) > 21:
                result = result + 1
            else:
                result = result + value

        return result


class Deck:
    def __init__(self):
        self.cards = self.create_deck()

    def get_card(self):
        if len(self.cards) < (settings.COUNT_CARD_IN_STANDART_DECK * settings.COUNT_DECKS / 2):
            self.create_deck()
        return self.cards.pop(random.randrange(0, len(self.cards)))

    def create_deck(self):
        self.cards = []
        for card in temlate_deck:
            for i in range(settings.COUNT_DECKS * 4):
                self.cards.append(card)
        return self.cards
