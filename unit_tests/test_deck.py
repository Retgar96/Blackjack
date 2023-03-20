from models.deck import template_deck
import unittest
from models.deck import Deck
from models.card import Card
import settings


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_creation(self):
        self.assertEqual(len(self.deck), settings.COUNT_CARD_IN_NORM_DECK * settings.COUNT_DECKS)

    def test_get_card(self):
        count_cards_before = len(self.deck)
        card = self.deck.get_card()
        count_cards_after = len(self.deck)
        self.assertEqual(count_cards_before - 1, count_cards_after)
        self.assertIsInstance(card, Card)
        self.assertIn(card, self.deck._cards)
        self.assertEqual(len(self.deck), settings.COUNT_CARD_IN_NORM_DECK * settings.COUNT_DECKS - 1)

    def test_deck_recreation(self):
        deck = Deck()
        for i in range(int(((settings.COUNT_CARD_IN_NORM_DECK * settings.COUNT_DECKS)/2)+1)):
            deck.get_card()
        self.assertEqual(settings.COUNT_CARD_IN_NORM_DECK * settings.COUNT_DECKS-1, len(deck))

    def test_str_method(self):
        self.assertEqual(str(self.deck), f'Count card:{len(self.deck)}')

    def test_get_card_returns_correct_card(self):
        card = self.deck.get_card()
        self.assertIn(card, template_deck)

    def test_create_deck_with_multiple_decks(self):
        settings.COUNT_DECKS = 2
        self.deck._create_deck()
        self.assertEqual(len(self.deck._cards), len(template_deck) * 8)

    # def test_create_deck_with_negative_decks(self):
    #     settings.COUNT_DECKS = -1
    #     with self.assertRaises(ValueError):
    #         self.deck._create_deck()

    def test_new_deck_has_correct_number_of_cards(self):
        deck = Deck()
        self.assertEqual(len(deck._cards), settings.COUNT_CARD_IN_NORM_DECK * settings.COUNT_DECKS)

    def test_get_card_returns_card_from_top_of_deck(self):
        deck = Deck()
        top_card = deck._cards[0]
        self.assertEqual(deck.get_card(), top_card)

    def test_get_card_decrements_card_count_by_one(self):
        deck = Deck()
        num_cards = len(deck._cards)
        deck.get_card()
        self.assertEqual(len(deck._cards), num_cards - 1)

    def test_second_instance_of_deck_is_same_as_first(self):
        deck1 = Deck()
        deck2 = Deck()
        self.assertIs(deck1, deck2)
