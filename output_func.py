def output(text):
    print("\033[34m {}".format(text+'\n'))


def out_red(text):
    print("\033[31m {}".format(text+'\n'))


def out_yellow(text):
    print("\033[33m {}".format(text))


def out_green(text):
    print("\033[32m {}".format(text))


def my_input(text):
    try:
        value = int(input(f'{text}\n'))
    except ValueError:
        out_red('Пожалуйста введите целое положительное число!')
        my_input(text)
    else:
        if value >= 0:
            return value
        else:
            out_red('Пожалуйста введите целое положительное число!')
            my_input(text)


def my_input_player_action(text):
    try:
        value = int(input(f'{text}\n'))
    except ValueError:
        out_red('Пожалуйста введите - 0 либо - 1')
        my_input(text)
    else:
        if value > 0:
            return value
        else:
            out_red('Пожалуйста введите - 0 либо - 1')
            my_input(text)