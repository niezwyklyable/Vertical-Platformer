from .sprite import Sprite
from .constants import BAT_LEFT_LIST, BAT_RIGHT_LIST, LEVEL_2_CHECKPOINT, LEVEL_3_CHECKPOINT, \
LEVEL_4_CHECKPOINT, GAME_OVER_CHECKPOINT, BIRD_LEFT_LIST, BIRD_RIGHT_LIST, \
GHOST_RIGHT_LIST, GHOST_LEFT_LIST, SKULL_LEFT_LIST, SKULL_RIGHT_LIST, WIDTH

class Enemy(Sprite):
    def __init__(self, x, y, dir, altitude):
        super().__init__(IMG_LIST=BAT_RIGHT_LIST, TYPE='ENEMY', x=x, y=y)
        self.dX = 2
        self.dir = dir
        if dir == 'left':
            self.IMG_TUPLE = tuple(BAT_LEFT_LIST)
            self.IMG = self.IMG_TUPLE[0]
        self.altitude = altitude
        self.SUBTYPE = self.set_subtype(dir, altitude)

    def set_subtype(self, dir, altitude):
        if altitude > LEVEL_2_CHECKPOINT and altitude < LEVEL_3_CHECKPOINT:
            if dir == 'right':
                self.IMG_TUPLE = tuple(BIRD_RIGHT_LIST)
            else:
                self.IMG_TUPLE = tuple(BIRD_LEFT_LIST)
            self.IMG = self.IMG_TUPLE[0]
            return 'BIRD'
        elif altitude > LEVEL_3_CHECKPOINT and altitude < LEVEL_4_CHECKPOINT:
            if dir == 'right':
                self.IMG_TUPLE = tuple(GHOST_RIGHT_LIST)
            else:
                self.IMG_TUPLE = tuple(GHOST_LEFT_LIST)
            self.IMG = self.IMG_TUPLE[0]
            return 'GHOST'
        elif altitude > LEVEL_4_CHECKPOINT and altitude < GAME_OVER_CHECKPOINT:
            if dir == 'right':
                self.IMG_TUPLE = tuple(SKULL_RIGHT_LIST)
            else:
                self.IMG_TUPLE = tuple(SKULL_LEFT_LIST)
            self.IMG = self.IMG_TUPLE[0]
            return 'SKULL'
        else:
            return 'BAT'
        
    def move(self):
        if self.dir == 'left':
            self.x -= self.dX
            # check boundaries
            if self.x < self.IMG.get_width()//2:
                self.x = self.IMG.get_width()//2
                self.dir = 'right'
                self.img_counter = 0
                if self.SUBTYPE == 'BAT':
                    self.IMG_TUPLE = tuple(BAT_RIGHT_LIST)
                elif self.SUBTYPE == 'BIRD':
                    self.IMG_TUPLE = tuple(BIRD_RIGHT_LIST)
                elif self.SUBTYPE == 'GHOST':
                    self.IMG_TUPLE = tuple(GHOST_RIGHT_LIST)
                elif self.SUBTYPE == 'SKULL':
                    self.IMG_TUPLE = tuple(SKULL_RIGHT_LIST)
                self.IMG = self.IMG_TUPLE[0]
        elif self.dir == 'right':
            self.x += self.dX
            # check boundaries
            if self.x > WIDTH - self.IMG.get_width()//2:
                self.x = WIDTH - self.IMG.get_width()//2
                self.dir = 'left'
                self.img_counter = 0
                if self.SUBTYPE == 'BAT':
                    self.IMG_TUPLE = tuple(BAT_LEFT_LIST)
                elif self.SUBTYPE == 'BIRD':
                    self.IMG_TUPLE = tuple(BIRD_LEFT_LIST)
                elif self.SUBTYPE == 'GHOST':
                    self.IMG_TUPLE = tuple(GHOST_LEFT_LIST)
                elif self.SUBTYPE == 'SKULL':
                    self.IMG_TUPLE = tuple(SKULL_LEFT_LIST)
                self.IMG = self.IMG_TUPLE[0]
                