from src.game import Game
from src.infrastructure import infrastructure

if __name__ == '__main__':
    game = Game(infrastructure())
    game.loop()