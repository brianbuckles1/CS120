import pygame

import simpleGE

class Gladiator(simpleGE.Sprite):
    """
    Gladiator class
    """
    def __init__(self, scene:simpleGE.Scene):
        """
        Initialize the Gladiator
        """
        super().__init__(scene)

        # set the image
        self.walkingSheet = simpleGE.SpriteSheet("../assets/hero-walking.png", (64,64),4, 9,.1)

        self.walkingCol=1
        self.walkingRow = 2
        self.moveSpeed = 2


    def process(self):
        self.dx=0
        self.dy=0
        walking=False

        if self.isKeyPressed(pygame.K_UP):
            self.walkingRow=0
            self.dy=-self.moveSpeed
            walking = True

        if self.isKeyPressed(pygame.K_DOWN):
            self.walkingRow=2
            self.dy=self.moveSpeed
            walking = True

        if self.isKeyPressed(pygame.K_LEFT):
            self.walkingRow=1
            self.dx=-self.moveSpeed
            walking = True

        if self.isKeyPressed(pygame.K_RIGHT):
            self.walkingRow=3
            self.dx=self.moveSpeed
            walking = True

        if walking:
            self.copyImage(self.walkingSheet.getNext(self.walkingRow))
        else:
            self.copyImage(self.walkingSheet.getCellImage(self.walkingRow,1))