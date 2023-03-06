from presenter.presenter import Game
from models.player import Player
from view.console_controller import Controller


if __name__ == '__main__':
    while True:
        player = Player(Controller.get_bank())
        game = Game(player)
        game.start_game()
