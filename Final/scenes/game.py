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

        self.bgMusic = simpleGE.Music("assets/background.wav",-1)
        self.bgMusic.play()

        start_sound = simpleGE.Sound("assets/fight.ogg")
        start_sound.play()

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
        self.lbl_score.text = f"Score: {self.__score}"
        self.lbl_score.center = (900, 750)
        self.sprites.append(self.lbl_score)

        self.lives = 3
        self.hearts = []
        for i in range(3):
            heart = Health(self, (50 + (i*50), 740))
            self.sprites.append(heart)
            self.hearts.append(heart)

        # create the enemies
        for i in range(10):
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
                if enemy.collidesWith(self.hit_box):
                    enemy.reset()
                    self.__score += 1
                    self.lbl_score.text = f"Score: {self.__score}"

            #break out or it will take lives
            return
        else:
            self.hit_box.hide()

        for enemy in self.enemies:
            enemy.moveTowardSprite(self.gladiator)
            if enemy.collidesWith(self.gladiator) and self.lives >0:
                self.lives -= 1
                self.hearts[self.lives].hide()
                enemy.reset()

        if self.lives == 0:
            self.game_over_sound.play()
            time.sleep(3)
            self.stop()

if __name__ == "__main__":
    game = Game()
    game.start()