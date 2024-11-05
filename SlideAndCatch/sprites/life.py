import simpleGE, pygame

"""
    miner.py

    Miner Sprite class that inherits from simpleGE.Sprite. 
"""


class Life(simpleGE.Sprite):
    """
    life sprite
    """

    def __init__(self, scene, center:(int,int) = (750, 40)):
        """
        Initializer
        :param scene:
        """
        super().__init__(scene)

        self.setImage("assets/miner.png")
        self.setSize(70, 55)
        self.position = center
