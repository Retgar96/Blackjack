import unittest
from models.player import Player, Bet, Hand, Status


class TestPlayer(unittest.TestCase):

    def test_status_full_lose(self):
        player = Player(1)
        player.bet = 1
        player.lose()
        self.assertEqual(player.status, Status.FullLose)

    def test_init(self):
        with self.assertRaises(TypeError):
            player = Player('100')

        with self.assertRaises(ValueError):
            player = Player(-1)

    def test_status_playing(self):
        player = Player(10)
        self.assertEqual(player.status, Status.Playing)

    def test_bank(self):
        player = Player(50)
        self.assertEqual(player.bank, 50)

    def test_win(self):
        player = Player(50)
        player.bet = 10
        player.win()
        self.assertEqual(player.bank, 60)

    def test_lose_full_lose(self):
        player = Player(10)
        player.bet = 10
        player.lose()
        self.assertEqual(player.status, Status.FullLose)
        self.assertEqual(player.bank, 0)

    def test_bet(self):
        player = Player(1)
        with self.assertRaises(ValueError):
            player.bet = 2

        with self.assertRaises(TypeError):
            player.bet = '2'

        with self.assertRaises(ValueError):
            player.bet = -1

    def test_lose_playing(self):
        player = Player(50)
        player.bet = 20
        status = player.lose()
        self.assertEqual(status, Status.Playing)
        self.assertEqual(player.bank, 30)
