import pygame

import simpleGE

from enum import Enum

class FacingDirection(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

class Gladiator(simpleGE.Sprite):
    """
    Gladiator class
    """
    def __init__(self, scene:simpleGE.Scene):
        """
        Initialize the Gladiator
        """
        super().__init__(scene)

        # set the image assets
        self.walkingSheet = simpleGE.SpriteSheet("../assets/hero-walking.png", (64,64),4, 9,.1)
        self.walkingSheet.startCol=1

        self.attackingSheet = simpleGE.SpriteSheet("../assets/hero-attacking.png", (192, 192), 4, 6, .1)

        # set the sound assets
        self.attackSound = simpleGE.Sound("../assets/sword_sfx.wav")

        # set the initial variables
        self.walkingCol=1
        self.walkingRow = 2
        self.moveSpeed = 2
        self.attackDirection = FacingDirection.UP

    def process(self):
        self.dx=0
        self.dy=0
        walking=False
        attacking=False

        # if the up arrow key is pressed, move up
        if self.isKeyPressed(pygame.K_UP):
            self.walkingRow=0
            self.dy=-self.moveSpeed
            self.attackDirection = FacingDirection.UP
            walking = True

        # if the down arrow key is pressed, move down
        if self.isKeyPressed(pygame.K_DOWN):
            self.walkingRow=2
            self.dy=self.moveSpeed
            self.attackDirection = FacingDirection.DOWN
            walking = True

        # if the left arrow key is pressed, move left
        if self.isKeyPressed(pygame.K_LEFT):
            self.walkingRow=1
            self.dx=-self.moveSpeed
            self.attackDirection = FacingDirection.LEFT
            walking = True

        # if the right arrow key is pressed, move right
        if self.isKeyPressed(pygame.K_RIGHT):
            self.walkingRow=3
            self.dx=self.moveSpeed
            self.attackDirection = FacingDirection.RIGHT
            walking = True

        # if the space bar is pressed, stop moving and attack
        if self.isKeyPressed(pygame.K_SPACE):
            self.dx=0
            self.dy=0
            attacking = True

        # if walking, set the image to the walking image
        if walking:
            self.copyImage(self.walkingSheet.getNext(self.walkingRow))
        else:
            print(self.walkingRow)
            self.copyImage(self.walkingSheet.getCellImage(0, self.walkingRow))

        # if attacking, set the image to the attacking image
        if attacking:
            self.copyImage(self.attackingSheet.getNext(self.attackDirection.value))

