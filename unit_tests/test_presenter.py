import unittest
from unittest.mock import patch, MagicMock
from models.player import Player
from presenter.presenter import Game
from models.status import Status


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player = Player(100)
        self.game = Game(self.player)

    @patch('presenter.presenter.Game._play_round')
    @patch('presenter.presenter.Controller.start_game')
    def test_start_game(self, mock_controller_start_game, mock_play_round):
        self.game.start_game()
        mock_controller_start_game.assert_called_once()
        mock_play_round.assert_called_once()

    @patch('presenter.presenter.Controller')
    def test_play_round_full_lose(self, mock_controller):
        self.game._desk.player = MagicMock()
        self.game._desk.player.status = Status.FullLose
        self.game._play_round()
        mock_controller.full_lose.assert_called_once()

    def test_play_round_win(self):
        self.game._desk.player = MagicMock()
        self.game._desk.player.hand.status = Status.Win
        self.game._place_bet = MagicMock()
        self.game._desk.deal_cards = MagicMock()
        self.game._win_player = MagicMock()
        self.game._play_round()
        self.game._desk.deal_cards.assert_called_once()
        self.game._win_player.assert_called_once()
        self.game._place_bet.assert_called_once()

    def test_play_round_playing(self):
        self.game._desk.player = MagicMock()
        self.game._desk.player.hand.status = Status
        self.game._place_bet = MagicMock()
        self.game._desk.deal_cards = MagicMock()
        self.game._action_player = MagicMock()
        self.game._play_round()
        self.game._desk.deal_cards.assert_called_once()
        self.game._action_player.assert_called_once()
        self.game._place_bet.assert_called_once()

    @patch('presenter.presenter.Controller')
    def test_place_bet_exception(self, mock_controller):
        mock_controller.get_bet.side_effect = Exception('bet exception')
        self.game._place_bet()
        mock_controller.error_message.assert_called_once()

    @patch('presenter.presenter.Controller')
    def test_place_bet_success(self, mock_controller):
        mock_controller.get_bet = 1
        self.game._place_bet()

    @patch('presenter.presenter.Controller')
    def test_action_player_get_card(self, mock_controller):
        mock_controller.action_bar.return_value = True
        self.game._desk.add_card_player = MagicMock()
        self.game._desk.player.hand = MagicMock()
        self.game._desk.player.hand.status = Status.Overdo
        self.game._lose_player = MagicMock()
        self.game._action_player()
        self.game._desk.add_card_player.assert_called_once()
        self.game._lose_player.assert_called_once()
        mock_controller.action_bar.assert_called_once()
        mock_controller.view_table.assert_called_once()

    @patch('presenter.presenter.Controller')
    def test_action_player_stop(self, mock_controller):
        mock_controller.action_bar.return_value = False
        self.game._action_dealer = MagicMock()
        self.game._action_player()
        self.game._action_dealer.assert_called_once()
        mock_controller.action_bar.assert_called_once()
        mock_controller.view_table.assert_called_once()

    @patch('presenter.presenter.Controller')
    def test_action_dealer_playing(self, mock_controller):
        self.game._desk.add_card_dealer = MagicMock()
        self.game._desk.dealer.hand = MagicMock()
        self.game._desk.dealer.hand.status = Status.DealerPlaying
        self.game._action_dealer()
        mock_controller.view_table.assert_called_once()

    def test_action_dealer_win(self):
        self.game._desk.add_card_dealer = MagicMock()
        self.game._desk.dealer.hand = MagicMock()
        self.game._lose_player = MagicMock()
        self.game._desk.dealer.hand.status = Status.Win
        self.game._action_dealer()
        self.game._lose_player.assert_called_once()

    def test_action_dealer_overdro(self):
        self.game._desk.add_card_dealer = MagicMock()
        self.game._desk.dealer.hand = MagicMock()
        self.game._win_player = MagicMock()
        self.game._desk.dealer.hand.status = Status.Overdo
        self.game._action_dealer()
        self.game._win_player.assert_called_once()
        self.game._desk.add_card_dealer.assert_called_once()

    def test_action_dealer_stop_win(self):
        self.game._desk.dealer.hand = MagicMock()
        self.game._desk.player.hand = MagicMock()
        self.game._desk.dealer.hand.score = 20
        self.game._desk.player.hand.score = 19
        self.game._desk.add_card_dealer = MagicMock()
        self.game._lose_player = MagicMock()
        self.game._desk.dealer.hand.status = Status
        self.game._action_dealer()
        self.game._desk.add_card_dealer.assert_called_once()
        self.game._lose_player.assert_called_once()


    def test_action_dealer_stop_lose(self):
        self.game._desk.dealer.hand = MagicMock()
        self.game._desk.player.hand = MagicMock()
        self.game._desk.dealer.hand.score = 19
        self.game._desk.player.hand.score = 20
        self.game._desk.add_card_dealer = MagicMock()
        self.game._win_player = MagicMock()
        self.game._desk.dealer.hand.status = Status
        self.game._action_dealer()
        self.game._desk.add_card_dealer.assert_called_once()
        self.game._win_player.assert_called_once()

