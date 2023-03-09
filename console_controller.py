from output_func import color_text


def start_game():
    print('Начнем игру!')


def get_bank():
    print('Введите cтартовый банк:')
    return get_value()


def get_bet():
    print('Введите сумму вашей ствки:')
    return get_value()


@color_text('red')
def error_message(type_error):
    print(type_error)


@color_text('yellow')
def view_table(table):
    print('_____________________________')
    dealer_card = []
    player_card = []
    for card in table['dealer']['card']:
        dealer_card.append(card.name)
    for card in table['player']['card']:
        player_card.append(card.name)

    print(f'Карта диллера: {dealer_card}: score: {table["dealer"]["score"]}')
    print(f'Ваши карты: {player_card} Ваш счет: {table["player"]["score"]}')
    print('_____________________________')


# def action_bar(self):
#     return self.__make_choice_action('Взять ещё карту - 1 \n Хватит - 0')

@color_text('green')
def win_action(bet, bank):
    print(f'Вы выйграли {bet}. Ваш баланс состовялет: {bank}')


@color_text('red')
def lose_action(bet, bank):
    print(f'Ваша ставка проиграла -{bet}. Ваш баланс состовляет: {bank}')


@color_text('red')
def full_lose():
    print('Вы проиграли игру, попробуйте ещё раз')


@color_text('red')
def make_choice_action():
    while True:
        value = input(f'Взять ещё карту - 1 \n Хватит - 0\n')
        if value != '0' and value != '1':
            print('Введите 1 либо 0!')
            continue
        else:
            break
    return bool(int(value))


@color_text('red')
def get_value():
    while True:
        try:
            value = int(input())
        except ValueError:
            print('Пожалуйста введите целое положительное число!')
            continue
        else:
            if value >= 0:
                return value
            else:
                print('Пожалуйста введите целое положительное число!')
                continue