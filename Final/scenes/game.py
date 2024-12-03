import time

import simpleGE
from sprites.gladiator import Gladiator, EnemyGladiator, PlayerAttackHitBox, PlayerHitBox
from sprites.health import Health


class Game(simpleGE.Scene):
    """
    Game class
    handles
    """
    def __init__(self,size=(1024,768)):
        """
        Game initialization method
        :param size: tuple of dimensions. Defaults 1024 x 768
        """
        super().__init__(size)
        self.sprites = []

        self.setImage("assets/background.png")

        # setup the background music
        self.bgMusic = simpleGE.Music("assets/background.wav",-1)
        self.bgMusic.play()

        # start fight sound
        start_sound = simpleGE.Sound("assets/fight.ogg")
        start_sound.play()

        # setup the game over sound
        self.game_over_sound = simpleGE.Sound("assets/game_over.ogg")

        # create the gladiators
        self.gladiator = Gladiator(self)
        self.gladiator.reset()
        self.sprites.append(self.gladiator)
        self.enemies = []

        self.playerHitBox = PlayerHitBox(self)
        self.playerHitBox.position = (self.gladiator.position[0], self.gladiator.position[1] + 10)
        self.sprites.append(self.playerHitBox)

        self.playerAttackHitBox = PlayerAttackHitBox(self)
        self.playerAttackHitBox.hide()
        self.sprites.append(self.playerAttackHitBox)
        self.__score = 0

        # create score label
        self.lbl_score = simpleGE.Label()
        self.__addScore(0)
        self.lbl_score.center = (900, 750)
        self.sprites.append(self.lbl_score)

        # create the lives
        self.hearts = []
        self.__setLives(self.gladiator.getLives())

        # create the enemies
        self.__createEnemies(2)

    def __addScore(self, num:int):
        """
        Update the score
        """
        self.__score += num
        self.lbl_score.text = f"Score: {self.__score}"

    def __playerHit(self):
        """
        Handle the player being hit
        """
        self.gladiator.lose_life()
        self.hearts[self.gladiator.getLives()].hide()

    def __setLives(self, num:int):
        """
        Set the number of lives
        """
        for i in range(num):
            heart = Health(self, (50 + (i * 50), 740))
            self.sprites.append(heart)
            self.hearts.append(heart)

    def __createEnemies(self, num:int):
        """
        Create the enemies
        """
        for i in range(num):
            print("Adding enemy")
            enemy = EnemyGladiator(self)
            enemy.reset()
            self.sprites.append(enemy)
            self.enemies.append(enemy)

    def get_score(self):
        """
        Get the current score
        """
        return self.__score

    def process(self):
        """
        Process the game
        """
        self.playerHitBox.position = (self.gladiator.position[0], self.gladiator.position[1] + 10)
        if self.gladiator.deathAnimationComplete():
            self.game_over_sound.play()
            time.sleep(1.5)  # wait for the sound to finish
            self.stop()
        if self.gladiator.isAttacking():
            self.playerAttackHitBox.show()
            self.playerAttackHitBox.setPosition(self.gladiator, self.gladiator.getFacingDirection())

            for enemy in self.enemies:
                self.__checkPlayerHitBoxCollision(enemy)
        else:
            self.playerAttackHitBox.hide()

            for enemy in self.enemies:
                enemy.moveTowardSprite(self.gladiator)
                enemy.setAnimationDirection(enemy.getDirectionToSprite(self.gladiator))
                self.__checkEnemyToPlayCollision(enemy)

    def __checkPlayerHitBoxCollision(self,enemy:EnemyGladiator):
        """
        Check if the player's hit box collides with the enemy
        """
        if self.playerAttackHitBox.collidesWith(enemy):
            enemy.reset()
            self.__addScore(1)

    def __checkEnemyToPlayCollision(self,enemy:EnemyGladiator):
        """
        Check if the enemy collides with the player
        """
        if enemy.collidesWith(self.playerHitBox):
            self.__playerHit()
            enemy.reset()

if __name__ == "__main__":
    game = Game()
    game.start()