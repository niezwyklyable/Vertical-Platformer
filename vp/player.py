from .sprite import Sprite
from .constants import PLAYER_IDLE_RIGHT_LIST, WIDTH, PLAYER_IDLE_LEFT_LIST

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=PLAYER_IDLE_RIGHT_LIST, TYPE='PLAYER', x=x, y=y)
        self.dX = 4
        self.current_dir = 'right'

    # steering
    def move(self, dir):
        if dir == 'left':
            # check if there are correct assets
            if self.current_dir != dir:
                self.counter = 0
                self.IMG_TUPLE = tuple(PLAYER_IDLE_LEFT_LIST)
                self.IMG = self.IMG_TUPLE[0]
                self.current_dir = dir
            self.x -= self.dX
            # check boundaries
            if self.x < self.IMG.get_width()//2:
                self.x = self.IMG.get_width()//2
        elif dir == 'right':
            # check if there are correct assets
            if self.current_dir != dir:
                self.counter = 0
                self.IMG_TUPLE = tuple(PLAYER_IDLE_RIGHT_LIST)
                self.IMG = self.IMG_TUPLE[0]
                self.current_dir = dir
            self.x += self.dX
            # check boundaries
            if self.x > WIDTH - self.IMG.get_width()//2:
                self.x = WIDTH - self.IMG.get_width()//2
        elif dir == 'up':
            pass
            