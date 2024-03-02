from .sprite import Sprite
from .constants import STEEL_PAD_LIST

class Pad(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=STEEL_PAD_LIST, TYPE='PAD', x=x, y=y)
        self.landed = False # if it is True that means the player landed on it and the player is able to fall down
        