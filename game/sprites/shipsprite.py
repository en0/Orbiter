import pygame
from game.sprites import Sprite
from game.shared import GameConstance

class ShipSprite(Sprite):
    def __init__(self, game):

        self.__gfx_ship = pygame.image.load(
            GameConstance.SHIP_SPRITE)
        self.__gfx_thrust = pygame.image.load(
            GameConstance.SHIP_THRUST_SPRITE)
        self.__gfx_shield = pygame.image.load(
            GameConstance.SHIP_SHIELD_SPRITE)
        self.__gfx_shield_thrust = pygame.image.load(
            GameConstance.SHIP_SHIELD_THRUST_SPRITE)


        super(ShipSprite, self).__init__(
            game,
            self.__gfx_ship
        )

        self.__thrust = False
        self.__shield = False
        self.__force = 0
        self.__fuel = 100.0
        self.__shields = 100.0
        self.__health = 100.0
        self.__mpg = 0.1

    @property
    def thrust(self):
        return self.__thrust

    @thrust.setter
    def thrust(self, value):
        self.__thrust = value

    @property
    def shield(self):
        return self.__shield

    @shield.setter
    def shield(self, value):
        self.__shield = value

    @property
    def fuel(self):
        return self.__fuel

    @property
    def shields(self):
        return self.__shields

    @property
    def health(self):
        return self.__health

    @property
    def isdead(self):
        return self.__health <= 0

    @property
    def rect(self):
        _r = self.__gfx_ship.get_rect()
        _r.right, _r.top = self.position
        return _r

    def update(self):
        __gfx = 0
        if self.__thrust == True and self.__fuel > 0:
            __gfx|=1
            self.__force += 1
            self.__fuel -= self.__mpg
        else:
            self.__force -= 1

        if self.__shield == True and self.__shields > 0:
            __gfx|=2
            self.__shields -= 1
        elif self.__shield == False:
            self.__shields += 0.1
            if self.__shields > 100:
                self.__shields = 100

        if __gfx == 1:
            self.sprite = self.__gfx_thrust
        elif __gfx == 2:
            self.sprite = self.__gfx_shield
        elif __gfx == 3:
            self.sprite = self.__gfx_shield_thrust
        else:
            self.sprite = self.__gfx_ship

        x,y = self.position
        y -= self.__force * .1
        self.position = (x,y)

    def addfuel(self, value):
        self.__fuel += value
        if self.__fuel > 100:
            self.__fuel = 100

    def addhealth(self, value):
        self.__health += value
        if self.__health > 100:
            self.__health = 100

    def take_damage(self, value):
        if self.__shields > 0 and self.__shield:
            self.__shields -= (value * 0.5)
            if self.__shields < 0:
                self.__health -= (self.__shields * -1)
                self.__shields = 0
        else:
            self.__health -= value

