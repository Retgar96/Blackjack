from output_func import output, my_input, out_red, out_green, input_player_action


def start_game():
    output('Начнем игру!')


def get_bank():
    return my_input('Введите cтартовый банк:')


def get_bet():
    return my_input('Введите сумму вашей ствки:')


def error_message(type_error):
    out_red(type_error)


def view_table(table):
    print('_____________________________')
    dealer_card = []
    player_card = []
    for card in table['dealer']['card']:
        dealer_card.append(card.name)
    for card in table['player']['card']:
        player_card.append(card.name)

    output(f'Карта диллера: {dealer_card}: score: {table["dealer"]["score"]}')
    output(f'Ваши карты: {player_card} Ваш счет: {table["player"]["score"]}')
    print('_____________________________')


def action_bar():
    return input_player_action('Взять ещё карту - 1 \n Хватит - 0')


def win_action(bet, bank):
    out_green(f'Вы выйграли {bet}. Ваш баланс состовялет: {bank}')


def lose_action(bet, bank):
    out_red(f'Ваша ставка проиграла -{bet}. Ваш баланс состовляет: {bank}')


def full_lose():
    out_red('Вы проиграли игру, попробуйте ещё раз')
