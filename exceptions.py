import output_func


class BetExceptions(Exception):

    def __init__(self, *args):
        self.message = args[0] if args else 'Упс, непредвиденая проблема со ставкой'


class BetExcessError(BetExceptions):

    def __init__(self, *args):
        self.massage = args[0] if args else 'Ставка привышает баланс'


class BetTypeError(BetExceptions):

    def __init__(self, *args):
        self.massage = args[0] if args else 'Ставка привышает баланс'


class BetNegativeError(BetExceptions):
    def __init__(self, *args):
        self.message = args[0] if args else 'Ставка не может быть отритцательной'


class InputActionError(Exception):
    def __init__(self):
        output_func.out_red('Введите 1 или 0')
