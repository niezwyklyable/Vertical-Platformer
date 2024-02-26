from .sprite import Sprite
from .constants import PLAYER_IDLE_RIGHT_LIST, WIDTH, PLAYER_IDLE_LEFT_LIST, \
    PLAYER_RUN_LEFT_LIST, PLAYER_RUN_RIGHT_LIST

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=PLAYER_IDLE_RIGHT_LIST, TYPE='PLAYER', x=x, y=y)
        self.dX = 4
        self.last_dir = 'right'
        self.idle = True
        #self.states = ['idle', 'run', 'jump_straight', 'jump_across', 'fall', 'double_jump']
        #self.dirs = ['right', 'left']

    # steering
    def move(self, dir):
        if dir == 'left':
            # check if there are correct assets
            if self.idle or self.last_dir == 'right':
                self.img_counter = 0
                self.IMG_TUPLE = tuple(PLAYER_RUN_LEFT_LIST)
                self.IMG = self.IMG_TUPLE[0]
                self.idle = False
                self.last_dir = 'left'
            self.x -= self.dX
            # check boundaries
            if self.x < self.IMG.get_width()//2:
                self.x = self.IMG.get_width()//2
        elif dir == 'right':
            # check if there are correct assets
            if self.idle or self.last_dir == 'left':
                self.img_counter = 0
                self.IMG_TUPLE = tuple(PLAYER_RUN_RIGHT_LIST)
                self.IMG = self.IMG_TUPLE[0]
                self.idle = False
                self.last_dir = 'right'
            self.x += self.dX
            # check boundaries
            if self.x > WIDTH - self.IMG.get_width()//2:
                self.x = WIDTH - self.IMG.get_width()//2
        elif dir == 'up':
            pass

    def change_state(self, state):
        if state == 'idle' and not self.idle:
            self.img_counter = 0
            if self.last_dir == 'left':
                self.IMG_TUPLE = tuple(PLAYER_IDLE_LEFT_LIST)
            elif self.last_dir == 'right':
                self.IMG_TUPLE = tuple(PLAYER_IDLE_RIGHT_LIST)
            self.IMG = self.IMG_TUPLE[0]
            self.idle = True
