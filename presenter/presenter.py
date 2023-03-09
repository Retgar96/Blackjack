import settings
from view.console_controller import Controller
from models.desk import Desk
from models.status import Status


class Game:
    def __init__(self, player):
        self._desk = Desk(player)

    def start_game(self):
        Controller.start_game()
        self._play_round()

    def _play_round(self):
        while True:
            if self._desk.player.status == Status.FullLose:
                Controller.full_lose()
                break
            self._place_bet()
            self._desk.deal_cards()
            if self._desk.player.hand.status == Status.Win:
                self._win_player()
            else:
                self._action_player()
            if settings.DEBUG:
                break

    def _place_bet(self):
        while True:
            try:
                self._desk.player.bet = Controller.get_bet()
            except Exception as e:
                Controller.error_message(e)
                if settings.DEBUG:
                    break
                continue
            break

    def _action_player(self):
        while True:
            Controller.view_table(self._desk)
            if Controller.action_bar():
                self._desk.add_card_player()
                if self._desk.player.hand.status == Status.Overdo:
                    self._lose_player()
                    break
                if settings.DEBUG:
                    break
                continue
            else:
                self._action_dealer()
                break

    def _action_dealer(self):
        while True:
            self._desk.add_card_dealer()
            if self._desk.dealer.hand.status == Status.DealerPlaying:
                Controller.view_table(self._desk)
                if settings.DEBUG:
                    break
                continue
            elif self._desk.dealer.hand.status == Status.Win:
                self._lose_player()
            elif self._desk.dealer.hand.status == Status.Overdo:
                self._win_player()
            else:
                if self._desk.dealer.hand.score > self._desk.player.hand.score:
                    self._lose_player()
                else:
                    self._win_player()
            break

    def _win_player(self):
        Controller.view_table(self._desk)
        self._desk.player.win()
        Controller.win_action(self._desk)
        self._desk.clear_hands()

    def _lose_player(self):
        Controller.view_table(self._desk)
        self._desk.player.lose()
        Controller.lose_action(self._desk)
        self._desk.clear_hands()
