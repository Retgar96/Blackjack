from backend import Table
from output_func import output, my_input, out_red, out_green, input_player_action


class Controller:
    @staticmethod
    def start_game():
        output('Начнем игру!')

    @staticmethod
    def get_bank():
        return my_input('Введите cтартовый банк:')

    @staticmethod
    def get_bet():
        return my_input('Введите сумму вашей ствки:')

    @staticmethod
    def error_message(type_error):
        out_red(type_error)

    @staticmethod
    def view_table(table):
        print('_____________________________')
        output(f'Карта диллера: {table.dealer.hand}')
        output(f'Ваши карты: {table.player.hand}')
        print('_____________________________')

    @staticmethod
    def action_bar():
        return input_player_action('Взять ещё карту - 1 \n Хватит - 0')

    @staticmethod
    def win_action(table):
        out_green(f'Вы выйграли {table.player.bet}. Ваш баланс состовялет: {table.player.bank}')

    @staticmethod
    def lose_action(table):

        out_red(f'Ваша ставка проиграла -{table.player.bet}. Ваш баланс состовляет: {table.player.bank}')

    @staticmethod
    def full_lose(table):
        # Controller.view_table(table)
        out_red('Вы проиграли игру, попробуйте ещё раз')


