import pygame
import random

from game.scenes import Scene
from game.shared import GameConstance
from game.sprites import *

class PlayScene(Scene):
    def __init__(self, game):
        super(PlayScene, self).__init__(game)
        self.__background = pygame.image.load(GameConstance.BACKGROUND)
        self.__background_position = 0

        self.__ship = ShipSprite(game)
        self.__ship.position = (20,GameConstance.SCREEN_SIZE[1]/2)
        self.__enemies = []
        self.__spawn_enemy_at = random.randrange(10, 100)
        self.__spawn_fuel_at = random.randrange(500, 600)
        self.__cycles = 0

        self.__level = 1
        self.__score = 0
        self.__paused = False

        self.__enemy_spawn_rate = [
            (0,0),      ## Level 0
            (50,100),   ## Level 1
            (40,90),    ## Level 2
            (30,80),    ## Level 3
            (20,70),    ## Level 4
            (10,60),    ## Level 5
            (10,50),    ## Level 6
            (10,40),    ## Level 7
            (10,30),    ## Level 8
            (10,20),    ## Level 9
            (5,10),     ## Level 10
            (1,5),      ## Level DEATH
        ]

    def render_hud(self):
        fuel = int(self.__ship.fuel)
        shields = int(self.__ship.shields)
        health = int(self.__ship.health)
        self.addtext("Fuel:", (10,10), 30)
        self.addtext(str(fuel), (100, 10), 30)
        self.addtext("Shields:", (10,40), 30)
        self.addtext(str(shields), (100, 40), 30)
        self.addtext("Heath:", (10,70), 30)
        self.addtext(str(health), (100, 70), 30)
        self.addtext("Level:", (600, 10), 30)
        self.addtext(str(self.__level), (700, 10), 30)
        self.addtext("Score:", (600, 40), 30)
        self.addtext(str(int(self.__score)), (700, 40), 30)


    def render(self):

        self.render_hud()
        self.addsprite(self.__background, (self.__background_position,0))
        self.addsprite(self.__ship.sprite, self.__ship.position)

        for enemy in self.__enemies:
            self.addsprite(enemy.sprite, enemy.position)

        if self.__paused == True:
            self.addtext("Paused", (325, 250), 50)

        super(PlayScene, self).render()


    def update(self, events):

        super(PlayScene, self).update(events)
        if self.__paused == True:
            for event in events:
                if (event.type == pygame.KEYDOWN and
                    event.key == 112):
                    self.__paused = False
            return
            
        for event in events:

            if (event.type == pygame.KEYDOWN and event.key == 276):
                self.__ship.thrust_nx = True

            elif (event.type == pygame.KEYUP and event.key == 276):
                self.__ship.thrust_nx = False

            if (event.type == pygame.KEYDOWN and event.key == 275):
                self.__ship.thrust_x = True

            elif (event.type == pygame.KEYUP and event.key == 275):
                self.__ship.thrust_x = False

            if (event.type == pygame.KEYDOWN and event.key == 273):
                self.__ship.thrust = True

            elif (event.type == pygame.KEYUP and event.key == 273):
                self.__ship.thrust = False

            if (event.type == pygame.KEYDOWN and event.key == 32):
                self.__ship.shield = True

            elif (event.type == pygame.KEYUP and event.key == 32):
                self.__ship.shield = False

            if (event.type == pygame.KEYDOWN and event.key == 112):
                self.__paused = True


        if self.__ship.isdead:
            self.game.score = self.__score
            self.game.setscene(GameConstance.GAMEOVER_SCENE)
            return;

        self.__cycles += 1
        self.__score += .05

        self.__background_position -= 1
        if self.__background_position <= -3200:
            self.__background_position = 0

        if self.__cycles % self.__spawn_enemy_at == 0:
            low, high = self.__enemy_spawn_rate[self.__level]
            self.__spawn_enemy_at = random.randrange(low, high)
            if random.randrange(1, 100) % 6 == 0:
                self.__enemies.append(BombSprite(self.game))
            else:
                self.__enemies.append(RocketSprite(self.game))
                

        if self.__cycles % self.__spawn_fuel_at == 0:
            self.__spawn_fuel_at = random.randrange(400, 500)
            self.__enemies.append(FuelSprite(self.game))

        if self.__cycles > 1000:
            self.__enemies.append(HealthSprite(self.game))
            self.__cycles = 0

            print("Level Up!")
            self.__level += 1
            if self.__level >= len(self.__enemy_spawn_rate):
                self.__level = len(self.__enemy_spawn_rate) - 1


        self.__ship.update()
        if (self.__ship.position[1] > GameConstance.SCREEN_SIZE[1] or
            self.__ship.position[1] < -50):
            self.__ship.take_damage(25)

        self.__enemies = [enemy for enemy in self.__enemies if enemy.position[0] > -50]

        for enemy in self.__enemies:
            enemy.update()

        for enemy in self.__enemies:
            if self.__ship.collides(enemy):
                enemy.hit(self.__ship)
                _,y = enemy.position
                enemy.position = (-100, y)
                break;


