from random import randint

import pygame

import simpleGE

from enum import Enum

class FacingDirection(Enum):
    """
    FacingDirection Enum
    """
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
        self.walkingSheet = simpleGE.SpriteSheet("assets/hero-walking.png", (64,64),4, 9,.1)
        self.walkingSheet.startCol=1

        self.attackingSheet = simpleGE.SpriteSheet("assets/hero-attacking.png", (192, 192), 4, 6, .1)

        self.attack_sound = simpleGE.Sound("assets/sword_sfx.wav")

        # set the initial variables
        self.__walkingCol=1
        self.__walkingRow = 2
        self.__moveSpeed = 4
        self.__attackDirection = FacingDirection.UP
        self.__attackCol = 0
        self.__isAttacking = False

    def is_attacking(self):
        """
        Get if the gladiator is attacking
        """
        return self.__isAttacking

    def get_facing_direction(self) -> FacingDirection:
        """
        Get the direction the gladiator is facing
        """
        return self.__attackDirection

    def reset(self):
        """
        reset the gladiator to the center of the screen
        """
        self.position = (self.scene.screen.get_size()[0]//2, self.scene.screen.get_size()[1]//2)

    def process(self):
        """
        process the gladiator
        """
        self.dx=0
        self.dy=0
        walking=False

        # if the up arrow key is pressed, move up
        if self.isKeyPressed(pygame.K_UP):
            self.__walkingRow=0
            self.dy=-self.__moveSpeed
            self.__attackDirection = FacingDirection.UP
            walking = True

        # if the down arrow key is pressed, move down
        if self.isKeyPressed(pygame.K_DOWN):
            self.__walkingRow=2
            self.dy=self.__moveSpeed
            self.__attackDirection = FacingDirection.DOWN
            walking = True

        # if the left arrow key is pressed, move left
        if self.isKeyPressed(pygame.K_LEFT):
            self.__walkingRow=1
            self.dx=-self.__moveSpeed
            self.__attackDirection = FacingDirection.LEFT
            walking = True

        # if the right arrow key is pressed, move right
        if self.isKeyPressed(pygame.K_RIGHT):
            self.__walkingRow=3
            self.dx=self.__moveSpeed
            self.__attackDirection = FacingDirection.RIGHT
            walking = True

        # if the space bar is pressed, stop moving and attack
        if self.isKeyPressed(pygame.K_SPACE):
            self.dx=0
            self.dy=0
            self.__isAttacking = True

        # if walking, set the image to the walking image
        if walking:
            self.copyImage(self.walkingSheet.getNext(self.__walkingRow))
        else:
            self.copyImage(self.walkingSheet.getCellImage(0, self.__walkingRow))

        # if attacking, set the image to the attacking image
        if self.__isAttacking:

            # if self.__attackCol >= 6:
            if self.attackingSheet.isDone():
                self.__isAttacking = False
                self.__attackCol = 0
                self.attackingSheet.animCol=0
                self.attack_sound.play()
            else:
                self.copyImage(self.attackingSheet.getNext(self.__attackDirection.value))

class EnemyGladiator(simpleGE.Sprite):
    """
    Gladiator class
    """
    def __init__(self, scene:simpleGE.Scene):
        """
        Initialize the Gladiator
        """
        super().__init__(scene)

        # set the image assets
        self.walkingSheet = simpleGE.SpriteSheet("assets/enemy-walking.png", (64,64),4, 9,.1)
        self.walkingSheet.startCol=1
        self.speed = randint(3, 5)

    def process(self):
        """
        process the enemy gladiator
        """
        self.copyImage(self.walkingSheet.getNext(3))

    def reset(self):
        """
        reset the enemy gladiator to a random spawn point
        """
        spawn_point = randint(0, 3)
        if spawn_point == 0:
            self.position = (randint(0, self.scene.screen.get_size()[0]), 0)
        if spawn_point == 1:
            self.position = (randint(0, self.scene.screen.get_size()[0]), self.scene.screen.get_size()[1])
        if spawn_point == 2:
            self.position = (0, randint(0, self.scene.screen.get_size()[1]))
        if spawn_point == 3:
            self.position = (self.scene.screen.get_size()[0], randint(0, self.scene.screen.get_size()[1]))

class HitBox(simpleGE.Sprite):
    """
    HitBox class

    This class is used to detect if the gladiator is attacking an enemy
    """
    def __init__(self, scene: simpleGE.Scene):
        """
        Initialize the HitBox
        """
        super().__init__(scene)
        self.setSize(64, 20)

    def set_position(self, gladiator:simpleGE.Sprite, direction:FacingDirection):
        """
        Set the position of the hit box based on the direction the gladiator is facing
        """
        if direction == FacingDirection.DOWN:
            self.setSize(64, 20)
            self.position = (gladiator.x, gladiator.y + 30)

        if direction == FacingDirection.UP:
            self.setSize(64, 20)
            self.position = (gladiator.x, gladiator.y - 30)

        if direction == FacingDirection.LEFT:
            self.setSize(30, 64)
            self.position = (gladiator.x - 30, gladiator.y)

        if direction == FacingDirection.RIGHT:
            self.setSize(30, 64)
            self.position = (gladiator.x + 30, gladiator.y)