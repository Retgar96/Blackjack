import console_controller as controller
from backend import Table, Player, Hand, Deck
from exceptions import BetExceptions


class Game:
    def __init__(self):
        self.table = Table(self.start_game())

    def start_game(self):
        while True:
            player = Player(controller.get_bank())
            controller.start_game()
            self.table = Table(player)
            self.play_round()

    def play_round(self):
        while True:
            if not self.table.check_balance():
                controller.full_lose()
                self.table.clear_hands()
                break
            try:
                self.table.player.bet = controller.get_bet()
                # table.check_bet()
            except BetExceptions as e:
                controller.error_message(e)
                continue

            self.table.deal_cards()
            controller.view_table(self.set_tabler_info())

            if self.table.check_21_player():
                self.win_player()
                continue
            else:
                self.action_player()
                continue

    def action_player(self):
        while True:
            if controller.action_bar():
                self.table.add_card_player()
                controller.view_table(self.set_tabler_info())
                if self.table.check_break(self.table.player):
                    self.lose_player()
                else:
                    self.set_tabler_info()
                    continue
            else:
                self.action_dealer()
                break

    def action_dealer(self):
        while True:
            if self.table.check_break(self.table.hand_dealer): ##### Дописать класс!!!!
                self.win_player()
                break
            else:
                if self.table.check_score_dealer():
                    self.table.add_card_dealer()
                    controller.view_table(self.set_tabler_info())
                    continue
                else:
                    if self.table.hand_dealer > self.table.player.hand:
                        self.lose_player()
                        break
                    else:
                        self.win_player()
                        break

    def win_player(self):
        self.table.player.win()
        controller.win_action(bet=self.table.player.bet, bank=self.table.player.bank)

    def lose_player(self):
        self.table.player.lose()
        controller.lose_action(self.table.player.bet, self.table.player.bank)

    def set_tabler_info(self):
        table = {'bank': self.table.player.bank, 'dealer':
            {'card': self.table.hand_dealer,
             'score': self.table.get_score_dealer()},
                 'player': {'card': self.table.player.hand,
                            'score': self.table.player.hand.value}
                 }

        return table


if __name__ == '__main__':
    game = Game()
    game.start_game()
