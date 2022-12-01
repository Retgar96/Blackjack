import console_controller as controller
from backend import GameTable


def start(game_table):
    controller.start_game()
    game_table.bank = controller.get_bank()
    play_round(game_table)


def play_round(game_table):
    bet = controller.get_bet()
    game_table.bet = bet
    if not game_table.check_bet():
        controller.error_message(type_error='Bet exceeded')
        play_round(game_table)

    game_table.deal_cards()
    controller.view_table(set_tabler_info(game_table))
    if game_table.check_21_player():
        win_player(game_table)
    else:
        action_player(game_table)


def action_player(game_table):
    if controller.action_bar():
        game_table.add_card_player()
        controller.view_table(set_tabler_info(game_table))
        if game_table.check_break_player():
            lose_player(game_table)
        else:
            set_tabler_info(game_table)
            action_player(game_table)
    else:
        action_dealer(game_table)


def action_dealer(game_table):
    if game_table.check_break_dealer():
        win_player(game_table)
    else:
        if game_table.check_score_dealer():
            game_table.add_card_dealer()
            controller.view_table(set_tabler_info(game_table))
            action_dealer(game_table)
        else:
            if game_table.get_score_dealer() > game_table.get_score_player():
                lose_player(game_table)
            else:
                win_player(game_table)


def win_player(game_table):
    game_table.add_bet()
    controller.win_action(bet=game_table.bet, bank=game_table.bank)
    play_round(game_table)


def lose_player(game_table):
    game_table.minus_bet()
    controller.losse_action(game_table.bet, game_table.bank)
    if not game_table.check_balance():
        controller.full_losse()
        start(game_table)
    else:
        play_round(game_table)


def set_tabler_info(game_table):
    table = {'bank': game_table.bank, 'dealer': {'card': game_table.dealer_card,
                                                'score': game_table.get_score_dealer()},
             'player': {'card': game_table.player_card,
                        'score': game_table.get_score_player()}
             }

    return table


if __name__ == '__main__':
    game_table = GameTable()
    start(game_table)