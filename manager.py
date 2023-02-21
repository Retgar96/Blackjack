from console_controller import Controller
from backend import Table, Player, Status


class Game:
    def __init__(self, table: Table):
        self.table = table

    def start_game(self):
        Controller.start_game()
        self._play_round()

    def _play_round(self):
        while True:
            if self.table.player.status == Status.FullLose:
                Controller.full_lose()
                break
            self._place_bet()
            self.table.deal_cards()
            if self.table.player.hand.status == Status.Win:
                self._win_player()
            else:
                self._action_player()

    def _place_bet(self):
        while True:
            try:
                self.table.player.bet = Controller.get_bet()
            except Exception as e:
                Controller.error_message(e)
                continue
            break

    def _action_player(self):
        while True:
            Controller.view_table(self.table)
            if Controller.action_bar():
                self.table.add_card_player()
                if self.table.player.hand.status == Status.Overdo:
                    self._lose_player()
                    break
                continue
            else:
                self._action_dealer()
                break

    def _action_dealer(self):
        while True:
            self.table.add_card_dealer()
            if self.table.dealer.hand.status == Status.DealerPlaying:
                Controller.view_table(self.table)
                continue
            elif self.table.dealer.hand.status == Status.Win:
                self._lose_player()
            elif self.table.dealer.hand.status == Status.Overdo:
                self._win_player()
            else:
                if self.table.dealer.hand.score > self.table.player.hand.score:
                    self._lose_player()
                else:
                    self._win_player()
            break

    def _win_player(self):
        Controller.view_table(self.table)
        self.table.player.win()
        Controller.win_action(self.table)
        self.table.clear_hands()

    def _lose_player(self):
        Controller.view_table(self.table)
        self.table.player.lose()
        Controller.lose_action(self.table)
        self.table.clear_hands()


if __name__ == '__main__':
    while True:
        player = Player(Controller.get_bank())
        table = Table(player)
        game = Game(table)
        game.start_game()
