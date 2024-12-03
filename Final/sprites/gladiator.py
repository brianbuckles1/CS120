import time
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

class BaseGladiator(simpleGE.Sprite):
    """
    Base Gladiator class
    """

    def getDirectionToSprite(self, sprite:simpleGE.Sprite)->FacingDirection:
        """
        Get the direction to a sprite
        """
        moveXDirection = FacingDirection.LEFT
        moveYDirection = FacingDirection.UP
        moveDirection = FacingDirection.UP

        # no need to check if the sprite is hidden
        if self.visible:
            if self.y > sprite.y:
                moveYDirection = FacingDirection.UP
            elif self.y < sprite.y:
                moveYDirection = FacingDirection.DOWN

            if self.x > sprite.x:
                moveXDirection = FacingDirection.LEFT
            elif self.x < sprite.x:
                moveXDirection = FacingDirection.RIGHT

            distanceX = abs(self.x - sprite.x)
            distanceY = abs(self.y - sprite.y)

            if distanceX > distanceY:
                moveDirection = moveXDirection
            else:
                moveDirection = moveYDirection
        return moveDirection

class Gladiator(BaseGladiator):
    """
    Gladiator class
    """
    def __init__(self, scene:simpleGE.Scene, lives:int=3):
        """
        Initialize the Gladiator
        """
        super().__init__(scene)

        # set the image assets
        self.walkingSheet = simpleGE.SpriteSheet("assets/hero-walking.png", (64,64),4, 9,.1)
        self.walkingSheet.startCol=1

        self.attackingSheet = simpleGE.SpriteSheet("assets/hero-attacking.png", (192, 192), 4, 6, 0)
        self.attack_sound = simpleGE.Sound("assets/sword_sfx.wav")

        self.deathSheet = simpleGE.SpriteSheet("assets/hero-death.png", (64, 64), 1, 6, 0)

        # set the initial variables
        self.__walkingCol=1
        self.__walkingRow = 2
        self.__moveSpeed = 4
        self.__attackDirection = FacingDirection.UP
        self.__attackCol = 0
        self.__isAttacking = False
        self.__walking = False
        self.__death = False
        self.__lives = lives

    def isAttacking(self):
        """
        Get if the gladiator is attacking
        """
        return self.__isAttacking

    def isDead(self):
        """
        Get if the gladiator is dead
        """
        return self.__lives <= 0

    def deathAnimationComplete(self):
        """
        Get if the death animation is complete
        """
        return self.deathSheet.isDone()

    def lose_life(self):
        """
        Lose a life
        """
        if self.__lives > 0:
            self.__lives -= 1

        if self.__lives == 0:
            self.__death = True

    def getLives(self):
        """
        Get the number of lives
        """
        return self.__lives

    def getFacingDirection(self) -> FacingDirection:
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
        self.__walking = False
        self.dx=0
        self.dy=0

        if self.__death:
            self.copyImage(self.deathSheet.getNext(0))
        elif self.__isAttacking:
            if self.attackingSheet.isDone():
                self.__isAttacking = False
                self.__attackCol = 0
                self.attackingSheet.animCol=0
                self.attack_sound.play()
            else:
                self.copyImage(self.attackingSheet.getNext(self.__attackDirection.value))
        else:
            # if the up arrow key is pressed, move up
            if self.isKeyPressed(pygame.K_w):
                if self.y >= 100:
                    self.moveUpAction()

            # if the down arrow key is pressed, move down
            if self.isKeyPressed(pygame.K_s):
                if self.y <= self.scene.screen.get_size()[1]-100:
                    self.moveDownAction()

            # if the left arrow key is pressed, move left
            if self.isKeyPressed(pygame.K_a):
                if self.x >= 100:
                    self.moveLeftAction()

            # if the right arrow key is pressed, move right
            if self.isKeyPressed(pygame.K_d):
                if self.x <= self.scene.screen.get_size()[0]-100:
                    self.moveRightAction()

            # if the up arrow key is pressed, move up
            if self.isKeyPressed(pygame.K_UP):
                if self.y >= 100:
                    self.moveUpAction()

            # if the down arrow key is pressed, move down
            if self.isKeyPressed(pygame.K_DOWN):
                if self.y <= self.scene.screen.get_size()[1] - 100:
                    self.moveDownAction()

            # if the left arrow key is pressed, move left
            if self.isKeyPressed(pygame.K_LEFT):
                if self.x >= 100:
                    self.moveLeftAction()

            # if the right arrow key is pressed, move right
            if self.isKeyPressed(pygame.K_RIGHT):
                if self.x <= self.scene.screen.get_size()[0] - 100:
                    self.moveRightAction()

            # if the space bar is pressed, stop moving and attack
            if self.isKeyPressed(pygame.K_SPACE):
                self.attackAction()

            # if walking, set the image to the walking image
            if self.__walking:
                self.copyImage(self.walkingSheet.getNext(self.__walkingRow))
            else:
                self.copyImage(self.walkingSheet.getCellImage(0, self.__walkingRow))



    def moveUpAction(self):
        """
        move up action
        """
        self.__walkingRow = 0
        self.dy = -self.__moveSpeed
        self.__attackDirection = FacingDirection.UP
        self.__walking = True

    def moveDownAction(self):
        """
        move down action
        """
        self.__walkingRow = 2
        self.dy = self.__moveSpeed
        self.__attackDirection = FacingDirection.DOWN
        self.__walking = True

    def moveLeftAction(self):
        """
        move left action
        """
        self.__walkingRow = 1
        self.dx = -self.__moveSpeed
        self.__attackDirection = FacingDirection.LEFT
        self.__walking = True

    def moveRightAction(self):
        """
        move right action
        """
        self.__walkingRow = 3
        self.dx = self.__moveSpeed
        self.__attackDirection = FacingDirection.RIGHT
        self.__walking = True

    def attackAction(self):
        """
        attack action
        """
        self.dx = 0
        self.dy = 0
        self.__isAttacking = True

class EnemyGladiator(BaseGladiator):
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
        self.speed = randint(3, 6)
        # self.speed =1

    def reset(self):
        """
        reset the enemy gladiator to a random spawn point
        """
        spawn_point = randint(0, 3)
        if spawn_point == 0:
            self.position = (randint(100, self.scene.screen.get_size()[0]), 100)
        if spawn_point == 1:
            self.position = (randint(100, self.scene.screen.get_size()[0]), self.scene.screen.get_size()[1]-100)
        if spawn_point == 2:
            self.position = (100, randint(0, self.scene.screen.get_size()[1]))
        if spawn_point == 3:
            self.position = (self.scene.screen.get_size()[0]-100 , randint(0, self.scene.screen.get_size()[1]))

    def setAnimationDirection(self, direction):
        """
        Set the direction of the sprite
        """

        if direction == FacingDirection.UP:
            self.copyImage(self.walkingSheet.getNext(0))

        if direction == FacingDirection.LEFT:
            self.copyImage(self.walkingSheet.getNext(1))

        if direction == FacingDirection.DOWN:
            self.copyImage(self.walkingSheet.getNext(2))

        if direction == FacingDirection.RIGHT:
            self.copyImage(self.walkingSheet.getNext(3))

class PlayerHitBox(simpleGE.Sprite):
    """
    HitBox class

    This class is used to detect if the gladiator is hit by an enemy
    """
    def __init__(self, scene: simpleGE.Scene):
        """
        Initialize the HitBox
        """
        super().__init__(scene)
        self.setSize(32, 50)

    def process(self):
        # hide the actual hit box from view but still check for collisions
        # we do not want to use the hide() method as it will not check for collisions
        self.image.set_alpha(0)

    def setPosition(self, gladiator:simpleGE.Sprite):
        """
        Set the position of the hit box to the gladiator
        """
        self.position = (gladiator.x, gladiator.y)

class PlayerAttackHitBox(simpleGE.Sprite):
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

    def process(self):
        # hide the actual hit box from view but still check for collisions
        # we do not want to use the hide() method as it will not check for collisions
        self.image.set_alpha(0)

    def setPosition(self, gladiator:simpleGE.Sprite, direction:FacingDirection):
        """
        Set the position of the hit box based on the direction the gladiator is facing
        """
        if direction == FacingDirection.DOWN:
            self.setSize(128, 50)
            self.position = (gladiator.x, gladiator.y + 30)

        if direction == FacingDirection.UP:
            self.setSize(128, 50)
            self.position = (gladiator.x, gladiator.y - 20)

        if direction == FacingDirection.LEFT:
            self.setSize(50, 128)
            self.position = (gladiator.x - 50, gladiator.y)

        if direction == FacingDirection.RIGHT:
            self.setSize(50, 128)
            self.position = (gladiator.x + 50, gladiator.y)