import console_controller as view
from backend import Table
from exceptions import BetExceptions


class Presenter:
    def __init__(self):
        self.table = Table()
        self.view = view
        self.__new_game()

    def __new_game(self):
        while True:
            self.table = Table()
            self.view.start_game()
            self.table.bank = view.get_bank()
            self.__play_round()

    def __play_round(self):
        while True:
            if not self.table.check_balance():
                self.view.full_lose()
                break
            self.table.clear_hands()
            bet = view.get_bet()
            self.table.bet = bet
            try:
                self.table.check_bet()
            except BetExceptions as e:
                view.error_message(e)
                continue

            self.table.deal_cards()
            view.view_table(set_tabler_info(self.table))
            if self.table.check_21_player():
                win_player(self.table)
                continue
            else:
                action_player(self.table)
                continue



def start():
    while True:
        game_table = Table()
        view.start_game()
        game_table.bank = view.get_bank()
        play_round(game_table)


def play_round(game_table):
    while True:
        if not game_table.check_balance():
            view.full_lose()
            break
        game_table.clear_hands()
        bet = view.get_bet()
        game_table.bet = bet
        try:
            game_table.check_bet()
        except BetExceptions as e:
            view.error_message(e)
            continue

        game_table.deal_cards()
        view.view_table(set_tabler_info(game_table))
        if game_table.check_21_player():
            win_player(game_table)
            continue
        else:
            action_player(game_table)
            continue


def action_player(game_table):
    while True:
        if view.action_bar():
            game_table.add_card_player()
            view.view_table(set_tabler_info(game_table))
            if game_table.check_break_player():
                lose_player(game_table)
            else:
                set_tabler_info(game_table)
                continue
        else:
            action_dealer(game_table)
            break


def action_dealer(game_table):
    while True:
        if game_table.check_break_dealer():
            win_player(game_table)
            break
        else:
            if game_table.check_score_dealer():
                game_table.add_card_dealer()
                view.view_table(set_tabler_info(game_table))
                continue
            else:
                if game_table.get_score_dealer() > game_table.get_score_player():
                    lose_player(game_table)
                    break
                else:
                    win_player(game_table)
                    break


def win_player(game_table):
    game_table.add_bet()
    view.win_action(bet=game_table.bet, bank=game_table.bank)


def lose_player(game_table):
    game_table.minus_bet()
    view.lose_action(game_table.bet, game_table.bank)


def set_tabler_info(game_table):
    table = {'bank': game_table.bank, 'dealer':
                {'card': game_table.dealer_card,
                 'score': game_table.get_score_dealer()},
            'player': {'card': game_table.player_card,
            'score': game_table.get_score_player()}
            }

    return table


if __name__ == '__main__':
    start()
