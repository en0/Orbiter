import os

class GameConstance():
    SCREEN_SIZE = (800, 600)

    MENU_SCENE = 0
    PLAY_SCENE = 1
    SETTING_SCENE = 2
    GAMEOVER_SCENE = 3
    HIGHSCORE_SCENE = 4

    BACKGROUND = os.path.join("game", "assets", "background2.png")

    SHIP_SPRITE = os.path.join("game","assets","ship.png")
    SHIP_SHIELD_SPRITE = os.path.join("game","assets","ship_shield.png")
    SHIP_THRUST_SPRITE = os.path.join("game","assets","flame.png")
    SHIP_SHIELD_THRUST_SPRITE = os.path.join("game","assets","flame_shield.png")
    ROCKET_SPRITE = os.path.join("game","assets","rocket.png")
    BOMB_SPRITE = os.path.join("game","assets","bomb.png")
    FUEL_SPRITE = os.path.join("game","assets","fuel.png")
    SHIELD_SPRITE = os.path.join("game","assets","shield.png")

    HIGHSCORE_FILE = os.path.join("game","assets","highscore.dat")

