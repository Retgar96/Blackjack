import unittest
from models.player import Player
from models.deck import Deck
from models.dealer import Dealer
from models.desk import Desk
import settings


class TestDesk(unittest.TestCase):
    def setUp(self):
        self.player = Player(100)
        self.desk = Desk(self.player)

    def test_init(self):
        self.assertEqual(self.desk.player, self.player)
        self.assertIsInstance(self.desk.deck, Deck)
        self.assertIsInstance(self.desk.dealer, Dealer)

    def test_clear_hands(self):
        self.desk.player.hand += self.desk.deck.get_card()
        self.desk.dealer.hand += self.desk.deck.get_card()
        self.desk.clear_hands()
        self.assertEqual(len(self.desk.player.hand), 0)
        self.assertEqual(len(self.desk.dealer.hand), 0)

    def test_deal_cards(self):
        self.desk.deal_cards()
        self.assertEqual(len(self.desk.player.hand), settings.STARTED_COUNT_CARD_IN_PLAYER_HAND)
        self.assertEqual(len(self.desk.dealer.hand), 1)
    #
    # def test_dealer_play(self):
    #     self.desk.dealer.hand += Card('10', 10)
    #     self.assertIsInstance(self.desk.dealer.hand.status, Status.DealerPlaying)
    #     self.desk.dealer.hand += Card('6', 6)
    #     self.assertIsInstance(self.desk.dealer.hand.status, Status.DealerPlaying)
    #     self.desk.dealer.hand += Card('7', 7)
    #     self.assertIsInstance(self.desk.dealer.hand.status, Status.DealerStop)
    #     self.desk.dealer.hand += Card('7', 7)
    #     self.assertIsInstance(self.desk.dealer.hand.status, Status.DealerStop)
    #
    # def test_player_play(self):
    #
    #     self.desk.player.hand += Card('10', 10)
    #     self.assertIsInstance(self.desk.player.hand.status, Status.Playing)
    #
    #     self.desk.player.hand += Card('10', 10)
    #     self.assertIsInstance(self.desk.player.hand.status, Status.Playing)
    #
    #     self.desk.player.hand += Card('10', 10)
    #     self.assertIsInstance(self.desk.player.hand.status, Status.Playing)


if __name__ == '__main__':
    unittest.main()
