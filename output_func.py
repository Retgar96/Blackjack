class Colors:
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


def color_text(color='white'):
    def retry_decorator(func):
        def _wrapper(*args, **kwargs):
            if color == 'red':
                print(f'{Colors.RED}')
            elif color == 'yellow':
                print(f'{Colors.YELLOW}')
            elif color == 'green':
                print(f'{Colors.GREEN}')
            else:
                print(Colors.ENDC)

            func(*args, **kwargs)
            print(f'{Colors.ENDC}\n')

        return _wrapper

    return retry_decorator