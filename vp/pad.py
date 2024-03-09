from .sprite import Sprite
from .constants import STEEL_PAD_LIST, LEVEL_2_CHECKPOINT, LEVEL_3_CHECKPOINT, \
LEVEL_4_CHECKPOINT, WOODEN_PAD_LIST, WIDTH, MEADOW_PAD_LIST, VOLCANIC_PAD_LIST, \
GAME_OVER_CHECKPOINT
from pygame.transform import scale

class Pad(Sprite):
    def __init__(self, x, y, w, altitude):
        super().__init__(IMG_LIST=STEEL_PAD_LIST, TYPE='PAD', x=x, y=y)
        self.landed = False # if it is True that means the player landed on it and the player is able to fall down
        self.w = w
        self.altitude = altitude
        self.level = self.set_level(altitude)
        self.resize(self.w)

    def resize(self, w):
        if w != self.IMG.get_width():
            NEW_IMG = scale(self.IMG, (w, self.IMG.get_height()))
            self.IMG = NEW_IMG
            self.IMG_TUPLE = tuple([self.IMG])

    def set_level(self, altitude):
        if altitude == LEVEL_2_CHECKPOINT:
            self.IMG_TUPLE = tuple(WOODEN_PAD_LIST)
            self.IMG = self.IMG_TUPLE[0]
            self.x = WIDTH//2
            self.w = WIDTH
            return 2
        elif altitude > LEVEL_2_CHECKPOINT and altitude < LEVEL_3_CHECKPOINT:
            self.IMG_TUPLE = tuple(WOODEN_PAD_LIST)
            self.IMG = self.IMG_TUPLE[0]
            return 2
        elif altitude == LEVEL_3_CHECKPOINT:
            self.IMG_TUPLE = tuple(MEADOW_PAD_LIST)
            self.IMG = self.IMG_TUPLE[0]
            self.x = WIDTH//2
            self.w = WIDTH
            return 3
        elif altitude > LEVEL_3_CHECKPOINT and altitude < LEVEL_4_CHECKPOINT:
            self.IMG_TUPLE = tuple(MEADOW_PAD_LIST)
            self.IMG = self.IMG_TUPLE[0]
            return 3
        elif altitude == LEVEL_4_CHECKPOINT:
            self.IMG_TUPLE = tuple(VOLCANIC_PAD_LIST)
            self.IMG = self.IMG_TUPLE[0]
            self.x = WIDTH//2
            self.w = WIDTH
            return 4
        elif altitude > LEVEL_4_CHECKPOINT and altitude < GAME_OVER_CHECKPOINT:
            self.IMG_TUPLE = tuple(VOLCANIC_PAD_LIST)
            self.IMG = self.IMG_TUPLE[0]
            return 4
        elif altitude == GAME_OVER_CHECKPOINT:
            self.IMG_TUPLE = tuple(VOLCANIC_PAD_LIST)
            self.IMG = self.IMG_TUPLE[0]
            self.x = WIDTH//2
            self.w = WIDTH
            return None
        else:
            return 1
        