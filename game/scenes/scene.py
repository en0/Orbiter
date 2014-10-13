import pygame

class Scene(object):

    def __init__(self, game):
        self.__game = game
        self.__render_sprites = []
        self.__render_text = []


    @property
    def game(self):
        return self.__game


    def update(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                exit()


    def render(self):
        surface = self.game.surface
        surface.fill((0,0,100))

        for sprite, pos in self.__render_sprites:
            surface.blit(sprite, pos)

        for text, pos in self.__render_text:
            surface.blit(text, pos)

        self.__render_sprites = []
        self.__render_text = []

        pygame.display.update()


    def addsprite(self, sprite, pos):
        self.__render_sprites.append((sprite, pos))


    def addtext(self, string, pos, size, color=None):
        if not color:
            color = (255,255,255)

        font = pygame.font.Font(None, size);
        text = font.render(string, 1, color)
        self.__render_text.append((text, pos))

