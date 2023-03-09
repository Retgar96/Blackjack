import unittest
from unittest.mock import patch

from models.card import Card
from models.deck import Deck
from models.desk import Desk
from models.hand import Hand
from models.player import Player
from presenter.presenter import Game
from models.status import Status
from view.console_controller import Controller


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player = Player('Test')
        self.game = Game(self.player)

    @patch('view.console_controller.Controller.start_game')
    @patch('game.Game._play_round')
    def test_start_game(self, mock_play_round, mock_start_game):
        self.game.start_game()
        mock_start_game.assert_called_once()
        mock_play_round.assert_called_once()

    @patch('view.console_controller.Controller.get_bet')
    @patch('view.console_controller.Controller.error_message')
    def test_place_bet(self, mock_error_message, mock_get_bet):
        mock_get_bet.side_effect = [50, ValueError, 100]
        self.game._place_bet()
        mock_get_bet.assert_called()
        mock_error_message.assert_called_once_with(ValueError())

    @patch('view.console_controller.Controller.view_table')
    @patch('view.console_controller.Controller.action_bar')
    @patch('game.Game._lose_player')
    @patch('game.Game._action_dealer')
    @patch('models.desk.Desk.deal_cards')
    @patch('game.Game._place_bet')
    def test_play_round(self, mock_place_bet, mock_deal_cards, mock_action_dealer,
                        mock_lose_player, mock_action_bar, mock_view_table):
        self.player.status = Status.FullLose
        self.game._play_round()
        mock_lose_player.assert_called_once()
        self.player.status = Status.Win
        self.game._play_round()
        self.game._win_player.assert_called_once()
        self.player.status = Status.Playing
        mock_action_bar.return_value = False
        self.game._play_round()
        mock_action_dealer.assert_called_once()
        self.player.hand.status = Status.Overdo
        self.game._play_round()
        mock_lose_player.assert_called_once()

    @patch('view.console_controller.Controller.view_table')
    @patch('models.desk.Desk.add_card_dealer')
    def test_action_dealer(self, mock_add_card_dealer, mock_view_table):
        self.player.hand.add_card('5')
        self.game._desk.dealer.hand.add_card('6')
        self.game._desk.dealer.hand.status = Status.DealerPlaying
        self.game._action_dealer()
        mock_add_card_dealer.assert_called_once()
        self.game._desk.dealer.hand.status = Status.Overdo
        self.game._action_dealer()
        self.game._win_player.assert_called_once()

    @patch('view.console_controller.Controller.view_table')
    @patch('models.desk.Desk.add_card_player')
    def test_action_player(self, mock_add_card_player, mock_view_table):
        self.game._desk.player.hand.add_card('5')
        self.game._desk.dealer.hand.add_card('6')
        self.game._desk.dealer.hand.status = Status.Win
        self.game._action_player()
        self.game._lose_player.assert_called_once()
        self.game._desk.dealer.hand.status = Status.DealerPlaying
        self.game._desk.player.hand.add_card('K')
        self.game._action_player()
        mock_add_card_player.assert_called_once()
        self.game._desk.player.hand.add_card('10')
        self.game._action_player()
        self.game._action_dealer.assert_called_once()

    @patch('view.console_controller.Controller.win_action')
    @patch('view.console_controller.Controller.view_table')
    def test_win_player(self, mock_view_table, mock_win_action):
        self.game._win_player()
        mock_win_action.assert_called_once()

    def test_init(self):
        self.assertIsInstance(self.game._desk, Desk)

    @patch('view.console_controller.Controller.start_game')
    @patch('game.game.Game._play_round')
    def test_start_game(self, mock_play_round, mock_start_game):
        self.game.start_game()
        mock_start_game.assert_called_once()
        mock_play_round.assert_called_once()

    @patch('view.console_controller.Controller.full_lose')
    def test_start_game_full_lose(self, mock_full_lose):
        self.game._desk.player.status = Status.FullLose
        self.game._play_round()
        mock_full_lose.assert_called_once()

    @patch('view.console_controller.Controller.get_bet')
    @patch('view.console_controller.Controller.error_message')
    def test_place_bet_error(self, mock_error_message, mock_get_bet):
        mock_get_bet.side_effect = ['invalid', 10]
        self.game._place_bet()
        self.assertEqual(mock_get_bet.call_count, 2)
        mock_error_message.assert_called_once()

    @patch('view.console_controller.Controller.view_table')
    @patch('view.console_controller.Controller.action_bar')
    def test_action_player_hit(self, mock_action_bar, mock_view_table):
        mock_action_bar.return_value = True
        self.game._desk.deck = Deck([Card('Heart', 2)])
        self.game._desk.player.hand = Hand([Card('Heart', 3)])
        self.game._action_player()
        self.assertEqual(len(self.game._desk.player.hand.cards), 2)

    @patch('game.game.Game._action_dealer')
    @patch('view.console_controller.Controller.view_table')
    @patch('view.console_controller.Controller.action_bar')
    def test_action_player_stand(self, mock_action_bar, mock_view_table, mock_action_dealer):
        mock_action_bar.return_value = False
        self.game._action_player()
        mock_action_dealer.assert_called_once()

    # @patch('view.console_controller.Controller.view_table')
    # def test_action_player
    #     mock_controller = mocker.patch.object(Controller, 'view_table')
    #     Game._win_player(Game(desk))
    #     assert desk.player.chips == 110
    #     assert mock_controller.call_count == 1
    #     assert mock_controller.call_args_list == [call(desk)]
    #
    # def test_lose_player(self, mocker):
    #     desk = Desk(Player("test_player"))
    #     desk.player.hand.add_card(Card(Suit.Hearts, Rank.Ace))
    #     desk.player.hand.add_card(Card(Suit.Clubs, Rank.King))
    #     desk.dealer.hand.add_card(Card(Suit.Diamonds, Rank.Jack))
    #     desk.dealer.hand.add_card(Card(Suit.Spades, Rank.Nine))
    #
    #     mock_controller = mocker.patch.object(Controller, 'view_table')
    #     Game._lose_player(Game(desk))
    #     assert desk.player.chips == 90
    #     assert mock_controller.call_count == 1
    #     assert mock_controller.call_args_list == [call(desk)]
    #
    # def test_play_round_full_lose(self, mocker):
    #     desk = Desk(Player("test_player"))
    #     desk.player.status = Status.FullLose
    #     game = Game(desk)
    #
    #     mock_controller_start_game = mocker.patch.object(Controller, 'start_game')
    #     mock_controller_full_lose = mocker.patch.object(Controller, 'full_lose')
    #     mock_place_bet = mocker.patch.object(game, '_place_bet')
    #     mock_deal_cards = mocker.patch.object(desk, 'deal_cards')
    #     mock_action_player = mocker.patch.object(game, '_action_player')
    #
    #     game._play_round()
    #
    #     mock_controller_start_game.assert_not_called()
    #     mock_controller_full_lose.assert_called_once()
    #     mock_place_bet.assert_not_called()
    #     mock_deal_cards.assert_not_called()
    #     mock_action_player.assert_not_called()
    #
    # def test_win_player(self, mocker):
    #     desk = Desk(Player("test_player"))
    #     desk.player.hand.add_card(Card(Suit.Hearts, Rank.Ace))
    #     desk.player.hand.add_card(Card(Suit.Clubs, Rank.King))
    #     desk.dealer.hand.add_card(Card(Suit.Diamonds, Rank.Jack))
    #     desk.dealer.hand.add_card(Card(Suit.Spades, Rank.Nine))
    #
    # game = Game(desk)
    #
    # mock_controller_start_game = mocker.patch.object(Controller, 'start_game')
    # mock_controller_full_lose = mocker.patch.object(Controller, 'full_lose')
    # mock_controller_view_table = mocker.patch.object(Controller, 'view_table')
    # mock_controller_get_bet = mocker.patch.object(Controller, 'get_bet', return_value=10)
    # mock_controller_action_bar = mocker.patch.object(Controller, 'action_bar', return_value=False)
    # mock_controller_win_action = mocker.patch.object(Controller, 'win_action')
    # mock_desk_add_card_player = mocker.patch.object(desk, 'add_card_player')
    # mock_desk_add_card_dealer = mocker.patch.object(desk, 'add_card_dealer')
    # mock_desk_clear_hands = mocker.patch.object(desk, 'clear_hands')
    #
    # game._play_round()
    #
    # mock_controller_start_game.assert_called_once()
    # mock_controller_full_lose.assert_not_called()
    # mock_controller_view_table.assert_has_calls([call(desk), call(desk)])
    # mock_controller_get_bet.assert_called_once()
    # mock_controller_action_bar.assert_called_once()
    # mock_controller_win_action.assert_called_once_with(desk)
    # mock_desk_add_card_player.assert_not_called()
    # mock_desk_add_card_dealer.assert_not_called()
    # mock_desk_clear_hands.assert_called_once()
    #
    # def test_play_round_lose_player(self, mocker):
    #     desk = Desk(Player("test_player"))
    #     desk.player.hand.add_card(Card(Suit.Hearts, Rank.Two))
    #     desk.player.hand.add_card(Card(Suit.Clubs, Rank.King))
    #     desk.dealer.hand.add_card(Card(Suit.Diamonds, Rank.Jack))
    #     desk.dealer.hand.add_card(Card(Suit.Spades, Rank.Nine))
    #     game = Game(desk)
    #
    #     mock_controller_start_game = mocker.patch.object(Controller, 'start_game')
    #     mock_controller_full_lose = mocker.patch.object(Controller, 'full_lose')
    #     mock_controller_view_table = mocker.patch.object(Controller, 'view_table')
    #     mock_controller_get_bet = mocker.patch.object(Controller, 'get_bet', return_value=10)
    #     mock_controller_action_bar = mocker.patch.object(Controller, 'action_bar', return_value=False)
    #     mock_controller_lose_action = mocker.patch.object(Controller, 'lose_action')
    #     mock_desk_add_card_player = mocker.patch.object(desk, 'add_card_player')
    #     mock_desk_add_card_dealer = mocker.patch.object(desk, 'add_card_dealer')
    #     mock_desk_clear_hands = mocker.patch.object(desk, 'clear_hands')
    #
    #     game._play_round()
    #
    #     mock_controller_start_game.assert_called_once()
    #     mock_controller_full_lose.assert_not_called()
    #     mock_controller_view_table.assert_has_calls([call(desk), call(desk)])
    #     mock_controller_get_bet.assert_called_once()
    #     mock_controller_action_bar.assert_called_once()
    #     mock_controller_lose_action.assert_called_once_with(desk)
    #     mock_desk_add_card_player.assert_not_called()
    #     mock_desk_add_card_dealer.assert_not_called()
    #     mock_desk_clear_hands.assert_called_once()


