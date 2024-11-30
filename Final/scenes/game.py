import time

import simpleGE
from sprites.gladiator import Gladiator,EnemyGladiator,HitBox
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
        self.hit_box = HitBox(self)
        self.hit_box.hide()
        self.sprites.append(self.hit_box)
        self.__score = 0

        # create score label
        self.lbl_score = simpleGE.Label()
        self.__addScore(0)
        self.lbl_score.center = (900, 750)
        self.sprites.append(self.lbl_score)

        self.lives = 3
        self.hearts = []
        self.__setLives(3)

        # create the enemies
        self.__createEnemies(4)

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
        self.lives -= 1
        self.hearts[self.lives].hide()
        self.__checkLives()

    def __setLives(self, num:int):
        """
        Set the number of lives
        """
        self.lives = num
        for i in range(num):
            heart = Health(self, (50 + (i * 50), 740))
            self.sprites.append(heart)
            self.hearts.append(heart)

    def __createEnemies(self, num:int):
        """
        Create the enemies
        """
        for i in range(num):
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
        if self.gladiator.is_attacking():
            self.hit_box.show()
            self.hit_box.set_position(self.gladiator, self.gladiator.get_facing_direction())

            for enemy in self.enemies:
                self.__checkPlayerHitBoxCollision(enemy)
        else:
            self.hit_box.hide()

            for enemy in self.enemies:
                enemy.moveTowardSprite(self.gladiator)
                enemy.setAnimationDirection(enemy.getDirectionToSprite(self.gladiator))
                self.__checkEnemyToPlayCollision(enemy)

    def __checkPlayerHitBoxCollision(self,enemy:EnemyGladiator):
        """
        Check if the player's hit box collides with the enemy
        """
        if self.hit_box.collidesWith(enemy):
            enemy.reset()
            self.__addScore(1)

    def __checkEnemyToPlayCollision(self,enemy:EnemyGladiator):
        """
        Check if the enemy collides with the player
        """
        if enemy.collidesWith(self.gladiator) and self.lives > 0:
            self.__playerHit()
            enemy.reset()

    def __checkLives(self):
        """
        Check the lives of the player
        """
        if self.lives == 0:
            self.game_over_sound.play()
            self.stop()

if __name__ == "__main__":
    game = Game()
    game.start()