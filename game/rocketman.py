import pygame
from game.shared import *
from game.scenes import *

class RocketMan():
    def __init__(self):

        ## Initialize PyGame
        pygame.init();
        self.__surface = pygame.display.set_mode(
            GameConstance.SCREEN_SIZE,
            pygame.DOUBLEBUF
        )

        ## Initialize clock
        self.__clock = pygame.time.Clock()

        ## Install Scenes
        self.__scene = None
        self.__current_scene = GameConstance.MENU_SCENE
        self.__scenes = [
            MenuScene,
            PlayScene,
            SettingsScene,
            GameOverScene,
            HighScoreScene,
        ]
        self.setscene(GameConstance.MENU_SCENE)

        self.__score = 0

    @property
    def scene(self):
        return self.__scene

    def setscene(self, value):
        print("Set new scene: " + str(value))
        self.__current_scene = value
        self.scene = self.__scenes[self.__current_scene](self)

    @property
    def surface(self):
        return self.__surface;

    @property
    def clock(self):
        return self.__clock

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def start(self):
        while True:
            self.clock.tick(50)
            scene = self.scene
            scene.update(pygame.event.get())
            scene.render()

