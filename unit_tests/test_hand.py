
# name_variations = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K']
# value_variations = [x for x in range(1, 10)]


import unittest
from models.card import Card
from models.status import Status
from models.hand import Hand


class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand = Hand()

    def test_add_card(self):
        card = Card('A', 11)
        self.hand += card
        self.assertEqual(len(self.hand), 1)

    def test_add_invalid_card(self):
        card = Card('A', 1)
        with self.assertRaises(ValueError):
            self.hand += card

    def test_add_wrong_type(self):
        with self.assertRaises(TypeError):
            self.hand += 'not a card'

    def test_calculate_score_with_one_ace(self):
        card1 = Card('A', 11)
        card2 = Card('D', 10)
        self.hand += card1
        self.hand += card2
        self.assertEqual(self.hand.score, 21)

    def test_calculate_score_with_2_ace_cards(self):
        for card in [Card('A', 11), Card('A', 11), Card('D', 10)]:
            self.hand += card

        self.assertEqual(self.hand.score, 22)

    def test_calculate_score_with_ace(self):
        for card in [Card('A', 11), Card('D', 10), Card('D', 10)]:
            self.hand += card
        self.assertEqual(self.hand.score, 21)

    def test_status_overdo(self):
        for card in [Card('9', 9), Card('D', 10), Card('D', 10)]:
            self.hand += card
        self.assertEqual(self.hand.score, 29)
        self.assertEqual(self.hand.status, Status.Overdo)

    def test_status_win(self):
        for card in [Card('D', 10), Card('A', 11)]:
            self.hand += card
        self.assertEqual(self.hand.status, Status.Win)

    def test_status_dealer_playing(self):
        for card in [Card('D', 10), Card('6', 6)]:
            self.hand += card
        self.assertEqual(self.hand.status, Status.DealerPlaying)

    def test_status_dealer_stop(self):
        for card in [Card('D', 10), Card('7', 7)]:
            self.hand += card
        self.assertEqual(self.hand.status, Status.DealerStop)

    def test_clean_hand(self):
        card = Card('4', 4)
        self.hand += card
        self.hand.clean()
        self.assertEqual(len(self.hand), 0)
        self.assertEqual(self.hand.score, 0)

    def tearDown(self):
        self.hand = None

if __name__ == '__main__':
    unittest.main()