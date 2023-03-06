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

    def deal_cards(self):
        self.dealer.hand += self.deck.get_card()
        for _ in range(settings.STARTED_COUNT_CARD_IN_PLAYER_HAND):
            self.player.hand += self.deck.get_card()

    def add_card_player(self):
        self.player.hand += self.deck.get_card()
        return self.player.hand.status

    def add_card_dealer(self):
        self.dealer.hand += self.deck.get_card()
