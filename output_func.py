def output(text):
    print(f'{Bcolors.CYAN}{text}{Bcolors.ENDC}\n')


def out_red(text):
    print(f'{Bcolors.RED}{text}{Bcolors.ENDC}\n')


def out_yellow(text):
    print(f'{Bcolors.YELLOW}{text}{Bcolors.ENDC}\n')


def out_green(text):
    print(f'{Bcolors.GREEN}{text}{Bcolors.ENDC}\n')


def input_player_action(text):
    while True:
        value = input(f'{text}\n')
        if value != '0' and value != '1':
            out_red('Введите 1 либо 0!')
            continue
        else:
            break
    return bool(int(value))


def my_input(text):
    while True:
        try:
            value = int(input(f'{text}\n'))
        except ValueError:
            out_red('Пожалуйста введите целое положительное число!')
            continue
        else:
            if value > 0:
                return value
            else:
                out_red('Пожалуйста введите целое положительное число!')
                continue


class Bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[31m'
    YELLOW = '\033[33m '
    UNDERLINE = '\033[4m'