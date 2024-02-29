from .sprite import Sprite
from .constants import PLAYER_IDLE_RIGHT_LIST, WIDTH, PLAYER_IDLE_LEFT_LIST, \
    PLAYER_RUN_LEFT_LIST, PLAYER_RUN_RIGHT_LIST, PLAYER_JUMP_LEFT_LIST, \
    PLAYER_JUMP_RIGHT_LIST, PLAYER_FALL_LEFT_LIST, PLAYER_FALL_RIGHT_LIST

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=PLAYER_IDLE_RIGHT_LIST, TYPE='PLAYER', x=x, y=y)
        self.dX = 4
        self.dY = 0
        self.last_dir = 'right'
        self.idle = True
        self.air = False
        self.fall = False
        self.G = 0.2 # gravitational accelaration
        self.F = -10 # initial jump force
        #self.states = ['idle', 'run', 'jump', 'fall', 'double_jump']
        #self.dirs = ['right', 'left']

    # steering
    def move(self, dir):
        if dir == 'left':
            # check if there are correct assets for the run state (on the ground only)
            if self.idle or self.last_dir == 'right' and not self.air:
                self.img_counter = 0
                self.IMG_TUPLE = tuple(PLAYER_RUN_LEFT_LIST)
                self.IMG = self.IMG_TUPLE[0]
                self.idle = False
                self.last_dir = 'left'
            # check if there are correct assets for the air state
            elif self.air and self.last_dir == 'right':
                self.img_counter = 0
                if self.fall:
                    self.IMG_TUPLE = tuple(PLAYER_FALL_LEFT_LIST)
                else:
                    self.IMG_TUPLE = tuple(PLAYER_JUMP_LEFT_LIST)
                self.IMG = self.IMG_TUPLE[0]
                self.idle = False
                self.last_dir = 'left'
            self.x -= self.dX
            # check boundaries
            if self.x < self.IMG.get_width()//2:
                self.x = self.IMG.get_width()//2
        elif dir == 'right':
            # check if there are correct assets for the run state (on the ground only)
            if self.idle or self.last_dir == 'left' and not self.air:
                self.img_counter = 0
                self.IMG_TUPLE = tuple(PLAYER_RUN_RIGHT_LIST)
                self.IMG = self.IMG_TUPLE[0]
                self.idle = False
                self.last_dir = 'right'
            # check if there are correct assets for the air state
            elif self.air and self.last_dir == 'left':
                self.img_counter = 0
                if self.fall:
                    self.IMG_TUPLE = tuple(PLAYER_FALL_RIGHT_LIST)
                else:
                    self.IMG_TUPLE = tuple(PLAYER_JUMP_RIGHT_LIST)
                self.IMG = self.IMG_TUPLE[0]
                self.idle = False
                self.last_dir = 'right'
            self.x += self.dX
            # check boundaries
            if self.x > WIDTH - self.IMG.get_width()//2:
                self.x = WIDTH - self.IMG.get_width()//2
        elif dir == 'jump':
            if not self.air:
                self.img_counter = 0
                if self.last_dir == 'left':
                    self.IMG_TUPLE = tuple(PLAYER_JUMP_LEFT_LIST)
                elif self.last_dir == 'right':
                    self.IMG_TUPLE = tuple(PLAYER_JUMP_RIGHT_LIST)
                self.IMG = self.IMG_TUPLE[0]
                self.idle = False
                self.air = True
                self.dY = self.F

    def change_state(self, state):
        if state == 'idle' and not self.idle and not self.air:
            self.img_counter = 0
            if self.last_dir == 'left':
                self.IMG_TUPLE = tuple(PLAYER_IDLE_LEFT_LIST)
            elif self.last_dir == 'right':
                self.IMG_TUPLE = tuple(PLAYER_IDLE_RIGHT_LIST)
            self.IMG = self.IMG_TUPLE[0]
            self.idle = True
        elif state == 'fall':
            self.img_counter = 0
            if self.last_dir == 'left':
                self.IMG_TUPLE = tuple(PLAYER_FALL_LEFT_LIST)
            elif self.last_dir == 'right':
                self.IMG_TUPLE = tuple(PLAYER_FALL_RIGHT_LIST)
            self.IMG = self.IMG_TUPLE[0]

    def gravity(self):
        if self.dY > 0 and not self.fall:
            self.air = True # it automatically turns on the air state when it detects falling
            self.fall = True
            self.change_state('fall')

        if self.air:
            self.dY += self.G
            self.y += self.dY
