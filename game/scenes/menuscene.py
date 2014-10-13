import pygame
from game.scenes import Scene
from game.shared import GameConstance

class MenuScene(Scene):

    def __init__(self, game):
        super(MenuScene, self).__init__(game)
        self.__selected = 0
        self.__menu = [
            ("Play", GameConstance.PLAY_SCENE),
            #("Settings", GameConstance.SETTING_SCENE),
            ("Exit", -1)
        ]


    def update(self, events):
        super(MenuScene, self).update(events)
        for event in events:
            if event.type == pygame.KEYDOWN:

                ## Check for enter
                if event.key == 13:
                    _, scene = self.__menu[self.__selected]
                    if scene < 0:
                        exit()
                    else:
                        self.game.setscene(scene)

                ## Check for down
                elif event.key == 274:
                    self.__selected += 1
                    if self.__selected >= len(self.__menu):
                        self.__selected = len(self.__menu) - 1

                ## Check for up
                elif event.key == 273:
                    self.__selected -= 1
                    if self.__selected <= 0:
                        self.__selected = 0


    def render(self):
        x,y,i = 200, 100, 0
        color = (255,255,255)

        for item, _ in self.__menu:

            if i == self.__selected:
                color = (0,255,0)
            else:
                color = (255,255,255)

            self.addtext(item, (x,y), 50, color=color)
            y += 50
            i += 1

        self.addtext("Rocket Man", (10,10), 50)
        super(MenuScene, self).render()

