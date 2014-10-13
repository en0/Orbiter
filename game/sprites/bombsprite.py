import pygame
import random
from game.sprites import Sprite
from game.shared import GameConstance

class BombSprite(Sprite):
    def __init__(self, game):
        self.__gfx1 = pygame.image.load(
            GameConstance.BOMB_SPRITE
        )
        super(BombSprite, self).__init__(
            game,
            self.__gfx1
        )
        self.position = (
            GameConstance.SCREEN_SIZE[0], 
            random.randrange(1, GameConstance.SCREEN_SIZE[1] - 32)
        )
        self.__speed = random.randrange(4,6)

    def update(self):
        x,y = self.position
        x-=self.__speed
        self.position = (x,y)

    def hit(self, ship):
        ship.take_damage(50)

