from models.player import Player
from models.deck import Deck
from models.dealer import Dealer
import settings


class Desk:
    def __init__(self, player: Player):
        self.player = player
        self.deck = Deck()
        self.dealer = Dealer()

    def clear_hands(self):
        self.player.hand.clean()
        self.dealer.hand.clean()

    def deal_cards(self):
        self.add_card_dealer()
        for _ in range(settings.STARTED_COUNT_CARD_IN_PLAYER_HAND):
            self.add_card_player()

    def add_card_player(self):
        self.player.hand += self.deck.get_card()
        return self.player.hand.status

    def add_card_dealer(self):
        self.dealer.hand += self.deck.get_card()
