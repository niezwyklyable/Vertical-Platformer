from .sprite import Sprite
from .constants import PLAYER_IDLE_LIST

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=PLAYER_IDLE_LIST, TYPE='PLAYER', x=x, y=y)

    # steering
    def move(self, dir):
        if dir == 'left':
            pass
        elif dir == 'right':
            pass
        elif dir == 'up':
            pass
            