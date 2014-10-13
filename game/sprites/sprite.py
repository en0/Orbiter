import pygame

class Sprite(object):
    def __init__(self, game, graphic):
        self.__game = game
        self.__graphic = graphic
        self.__position = (0,0)

    @property
    def sprite(self):
        return self.__graphic


    @sprite.setter
    def sprite(self, value):
        self.__graphic = value


    @property
    def game(self):
        return self.__game


    @property
    def position(self):
        return self.__position


    @position.setter
    def position(self, value):
        self.__position = value


    @property
    def rect(self):
        _r = self.__graphic.get_rect()
        _r.right, _r.top = self.position
        return _r

    
    def collides(self, obj):
        return self.rect.colliderect(obj.rect)


    def hit(self, obj):
        pass


    def update(self):
        pass
