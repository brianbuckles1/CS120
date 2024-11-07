from tabnanny import check

import simpleGE, sprites.miner,sprites.minerals, sprites.life, random
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
        self.__score = 0
        self.__lives_left = 3
        self.__total_gems = 5
        self.__total_rocks = 5
        self.sprites = []
        self.gems = []
        self.rocks = []

        self.lives = []
        self.__first_life = sprites.life.Life(self)
        self.lives.append(self.__first_life)
        self.sprites.append(self.__first_life)
        self.__second_life = sprites.life.Life(self,(680,40))
        self.lives.append(self.__second_life)
        self.sprites.append(self.__second_life)
        self.__third_life = sprites.life.Life(self, (610, 40))
        self.lives.append(self.__third_life)
        self.sprites.append(self.__third_life)

        self.sndGem = simpleGE.Sound("assets/bing1.wav")
        self.sndRock = simpleGE.Sound("assets/thud2.wav")

        # create the miner sprite
        self.__miner = sprites.miner.Miner(self)
        self.sprites.append(self.__miner)

        # create score label
        self.lbl_score = simpleGE.Label()
        self.lbl_score.set_font_size(30)
        self.lbl_score.size = (250,50)
        self.lbl_score.center = (100,28)
        self.lbl_score.text="Score: 0"
        self.sprites.append(self.lbl_score)

        # create gems
        for i in range(self.__total_gems):
            gem = sprites.minerals.Gem(self)
            self.sprites.append(gem)
            self.gems.append(gem)

        for i in range(self.__total_rocks):
            rock = sprites.minerals.Rock(self)
            self.sprites.append(rock)
            self.rocks.append(rock)
                

    def process(self):
        """
        Process
        Process the next frame cycle
        :return: void
        """

        # create score label
        self.lbl_score.text=f"Score: {self.__score}"

        for gem in self.gems:
            if gem.collidesWith(self.__miner):
                self.__score += 1
                self.sndGem.play()
                gem.reset()

        for rock in self.rocks:
            if rock.collidesWith(self.__miner):
                self.__lives_left -= 1
                self.lives[self.__lives_left].hide()
                self.sndRock.play()
                rock.reset()

            if self.__lives_left <= 0:
                self.stop()

    def get_score(self)->int:
        """
        get the score for the game
        :return: int
        """
        return self.__score