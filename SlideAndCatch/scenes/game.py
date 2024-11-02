from tabnanny import check

import simpleGE, sprites.miner,sprites.minerals, random
"""
    Game class
"""

class Game(simpleGE.Scene):
    """
    Game class
    handles create the game sprites and sounds and handling collisions
    """
    def __init__(self, size=(800,600)):
        """
        Game initialization method
        :param size: tuple of dimensions. Defaults 800 x 600
        """
        super().__init__(size)
        # setup scene
        self.setImage("assets/mine.png")
        self.setCaption("Gem Catcher")
        self.score = 0
        self.lives = 3
        self.totalMinerals = 10
        self.sprites = []
        self.gems = []
        self.rocks = []
        self.sndGem = simpleGE.Sound("assets/bing1.wav")
        self.sndRock = simpleGE.Sound("assets/thud2.wav")

        # create the miner sprite
        self.miner = sprites.miner.Miner(self)
        self.sprites.append(self.miner)

        # create minerals
        for i in range(self.totalMinerals):
            mineral_type = random.randint(1, 2)
            if mineral_type % 2 == 0:
                gem = sprites.minerals.Gem(self)
                self.sprites.append(gem)
                self.gems.append(gem)
            else:
                rock = sprites.minerals.Rock(self)
                self.sprites.append(rock)
                self.rocks.append(rock)

    def process(self):
        """
        Process
        Process the next frame cycle
        :return: void
        """
        for gem in self.gems:
            if gem.collidesWith(self.miner):
                self.score += 1
                self.sndGem.play()
                gem.reset()

        for rock in self.rocks:
            if rock.collidesWith(self.miner):
                self.lives -= 1
                self.sndRock.play()
                rock.reset()

