import pygame

from game.scenes import Scene
from game.shared import GameConstance

class HighScoreScene(Scene):
    def __init__(self, game):
        super(HighScoreScene, self).__init__(game)
        self.__scores = []
        with open(GameConstance.HIGHSCORE_FILE, "r") as fid:
            for line in fid:
                self.__scores.append(line.split('[::]'))
        self.__scores.sort(key=lambda tup: int(tup[1]), reverse=True)

    def render(self):
        y = 100
        i = 0
        for name, score in self.__scores:
            self.addtext(str(i+1), (300, y), 30)
            self.addtext(name, (340, y), 30)
            self.addtext(score[:-1], (440, y), 30)
            y+=30
            i+=1
            if i > 10:
                break

        self.addtext("High Scores", (10, 10), 50)
        super(HighScoreScene, self).render()

    def update(self, events):
        super(HighScoreScene, self).update(events)
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == 13:
                self.game.setscene(GameConstance.MENU_SCENE)

