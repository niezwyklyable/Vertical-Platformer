from .sprite import Sprite
from .constants import STEEL_PAD_LIST
from pygame.transform import scale

class Pad(Sprite):
    def __init__(self, x, y, w, altitude):
        super().__init__(IMG_LIST=STEEL_PAD_LIST, TYPE='PAD', x=x, y=y)
        self.landed = False # if it is True that means the player landed on it and the player is able to fall down
        self.w = w
        self.resize(w)
        self.altitude = altitude

    def resize(self, w):
        if w != self.IMG.get_width():
            NEW_IMG = scale(self.IMG, (w, self.IMG.get_height()))
            self.IMG = NEW_IMG
            self.IMG_TUPLE = tuple([self.IMG])
