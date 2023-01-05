import console_controller as controller
from backend import GameTable
from exceptions import BetExceptions


def start():
    while True:
        game_table = GameTable()
        controller.start_game()
        game_table.bank = controller.get_bank()
        play_round(game_table)


def play_round(game_table):
    while True:
        if not game_table.check_balance():
            controller.full_lose()
            break
        game_table.clear_hands()
        bet = controller.get_bet()
        game_table.bet = bet
        try:
            game_table.check_bet()
        except BetExceptions as e:
            controller.error_message(e)
            continue

        game_table.deal_cards()
        controller.view_table(set_tabler_info(game_table))
        if game_table.check_21_player():
            win_player(game_table)
            continue
        else:
            action_player(game_table)
            continue


def action_player(game_table):
    while True:
        if controller.action_bar():
            game_table.add_card_player()
            controller.view_table(set_tabler_info(game_table))
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
                controller.view_table(set_tabler_info(game_table))
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
    controller.win_action(bet=game_table.bet, bank=game_table.bank)


def lose_player(game_table):
    game_table.minus_bet()
    controller.lose_action(game_table.bet, game_table.bank)


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
