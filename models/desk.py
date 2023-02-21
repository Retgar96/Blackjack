from models.player import Player
from models.deck import Deck
from models.dealer import Dealer
import settings


class Desk:
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
