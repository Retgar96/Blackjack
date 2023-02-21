from console_controller import Controller
from backend import Table, Player, Hand, Deck, Status
from exceptions import BetExceptions


class Game:
    def __init__(self, table: Table):
        self.table = table

    def start_game(self):
        Controller.start_game()
        self._play_round()

    # def _create_player(self):
    #     self.table = Player(Controller.get_bank())

    # def _create_table(self):
    #     self.table = Table(self._create_player())

    def _play_round(self):
        while True:
            if self.table.player.status == Status.FullLose:
                Controller.full_lose(table)
                break
            self._place_bet()
            self.table.deal_cards()
        # controller.view_table(self.set_tabler_info())
            if self.table.player.hand.status == Status.Win:
                self._win_player()
            else:
                self._action_player()
        # while True:
        # if not self.table.check_player_balance():
        #     self.controller.full_lose()
        #     break

        # self._check_21_player()

        # if self.table.player.hand.status == Status.Win:
        #     self._win_player()
        #     continue
        # else:
        #     self._action_player()
        #     continue

    def _place_bet(self):
        while True:
            try:
                self.table.player.bet = Controller.get_bet()
            except Exception as e:
                Controller.error_message(e)
                continue
            break

    # def _check_21_player(self):
    #     pass

    def _action_player(self):
        while True:
            Controller.view_table(self.table)
            if Controller.action_bar():
                self.table.add_card_player()
                if self.table.player.hand.status == Status.Overdo:
                    self._lose_player()
                    # self.controller.view_table()
                    # if self.table.player.status == Status.FullLose:
                        # Controller.view_table(table)
                        # Controller.full_lose(table)
                    break
                continue
            else:
                self._action_dealer()
                break

    def _action_dealer(self):
        while True:
            # if self.table.check_break(): ##### Дописать класс!!!!
            #     self._win_player()
            #     break
            # else:
            #     if self.table.check_score_dealer():
            self.table.add_card_dealer()
            if self.table.dealer.hand.status == Status.DealerPlaying:
                # self.controller.view_table(self.set_tabler_info())
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

    # def _set_tabler_info(self):
    #     table = {'bank': self.table.player.bank, 'dealer':
    #         {'card': self.table.hand_dealer,
    #          'score': self.table.get_score_dealer()},
    #              'player': {'card': self.table.player.hand,
    #                         'score': self.table.player.hand.value}
    #              }
    #
    #     return table


if __name__ == '__main__':
    while True:
        player = Player(Controller.get_bank())
        table = Table(player)
        game = Game(table)
        game.start_game()
