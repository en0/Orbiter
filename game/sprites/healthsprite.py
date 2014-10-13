import pygame
import random

from game.sprites import Sprite
from game.shared import GameConstance

class HealthSprite(Sprite):
    def __init__(self, game):
        self.__gfx1 = pygame.image.load(
            GameConstance.SHIELD_SPRITE
        )
        super(HealthSprite, self).__init__(
            game,
            self.__gfx1
        )
        self.position = (
            GameConstance.SCREEN_SIZE[0], 
            random.randrange(1, GameConstance.SCREEN_SIZE[1] - 32)
        )
        self.__speed = random.randrange(1,2)

    def update(self):
        x,y = self.position
        x-=self.__speed
        self.position = (x,y)

    def hit(self, ship):
        print("Power up!")
        ship.addhealth(25)


