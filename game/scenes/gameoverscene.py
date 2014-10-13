import pygame
from game.scenes import Scene
from game.shared import GameConstance

class GameOverScene(Scene):
    def __init__(self, game):
        super(GameOverScene, self).__init__(game)
        self.__alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__name = ["[","-","-","-","]"]
        self.__index = 1
        self.__alpha_index = -1

    def render(self):
        self.addtext("Game Over", (300, 275), 50)
        self.addtext("Your Score: " + str(int(self.game.score)), (10, 10), 30)
        self.addtext("Submit your score: " + " ".join(self.__name), (10, 40), 30)
        super(GameOverScene, self).render()

    def update(self, events):
        super(GameOverScene, self).update(events)
        for event in events:
            if event.type == pygame.KEYDOWN:

                if event.key == 273:
                    self.__alpha_index += 1
                    if self.__alpha_index >= len(self.__alpha):
                        self.__alpha_index = 0

                elif event.key == 274:
                    self.__alpha_index -= 1
                    if self.__alpha_index < 0:
                        self.__alpha_index = len(self.__alpha) - 1

                elif event.key == 13:
                    self.__index+= 1
                    self.__alpha_index = -1
                    if self.__index == 4:
                        self.save_score()
                        self.game.setscene(GameConstance.HIGHSCORE_SCENE)

                elif event.key == 27:
                    self.game.setscene(GameConstance.MENU_SCENE)

        if self.__index <= 3 and self.__index >= 1:
            if self.__alpha_index > -1:
                self.__name[self.__index] = self.__alpha[self.__alpha_index]
            else:
                self.__name[self.__index] = "_"
        
    def save_score(self):
        with open(GameConstance.HIGHSCORE_FILE, "a") as fid:
            fid.write("".join(self.__name[1:4]))
            fid.write("[::]")
            fid.write(str(int(self.game.score)))
            fid.write("\n")
            

