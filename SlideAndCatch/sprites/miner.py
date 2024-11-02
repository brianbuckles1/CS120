import simpleGE, pygame

"""
    miner.py
    
    Miner Sprite class that inherits from simpleGE.Sprite. 
"""

class Miner(simpleGE.Sprite):
    """
    Miner sprite
    """
    def __init__(self, scene):
        """
        Initializer
        :param scene:
        """
        super().__init__(scene)

        self.setImage("assets/miner.png")
        self.setSize(125, 100)
        self.position = (360,550)
        self.moveSpeed = 5

    def process(self):
        """
        process event
        moves miner left or right based on the corresponding left key or right key
        :return: void
        """
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        elif self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed