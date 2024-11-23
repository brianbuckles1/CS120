import simpleGE
import sprites.gladiator
from sprites.gladiator import Gladiator


class Game(simpleGE.Scene):
    """
    Game class
    handles
    """
    def __init__(self,size=(800,400)):
        """
        Game initialization method
        :param size: tuple of dimensions. Defaults 800 x 600
        """
        super().__init__(size)

        # create the gladiators
        gladiator = Gladiator(self)
        self.sprites.append(gladiator)


if __name__ == "__main__":
    game = Game()
    game.start()