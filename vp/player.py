from .sprite import Sprite
from .constants import PLAYER_IDLE_RIGHT_LIST, WIDTH, PLAYER_IDLE_LEFT_LIST, \
    PLAYER_RUN_LEFT_LIST, PLAYER_RUN_RIGHT_LIST, PLAYER_JUMP_LEFT_LIST, \
    PLAYER_JUMP_RIGHT_LIST, PLAYER_FALL_LEFT_LIST, PLAYER_FALL_RIGHT_LIST, \
    PLAYER_DOUBLE_JUMP_LEFT_LIST, PLAYER_DOUBLE_JUMP_RIGHT_LIST

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
        self.F1 = -10 # initial jump force
        self.F2 = -5 # initial double jump force
        self.double_jump_counter = 0 # it increments when player is in the air until it reaches DOUBLE_JUMP_LIMIT
        self.DOUBLE_JUMP_LIMIT = 30 # after reaching that value player can perform double jump (double_jump_ready flag is on)
        self.double_jump_ready = False # as above
        self.double_jump_done = False # if True player cannot perform double jump (you can do it only once)

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
                if self.double_jump_done: # during performing double jump
                    self.IMG_TUPLE = tuple(PLAYER_DOUBLE_JUMP_LEFT_LIST)
                elif self.fall:
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
                if self.double_jump_done: # during performing double jump
                    self.IMG_TUPLE = tuple(PLAYER_DOUBLE_JUMP_RIGHT_LIST)
                elif self.fall:
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
                self.dY = self.F1
            elif self.double_jump_ready and self.air and not self.fall \
                and not self.double_jump_done:
                self.img_counter = 0
                if self.last_dir == 'left':
                    self.IMG_TUPLE = tuple(PLAYER_DOUBLE_JUMP_LEFT_LIST)
                elif self.last_dir == 'right':
                    self.IMG_TUPLE = tuple(PLAYER_DOUBLE_JUMP_RIGHT_LIST)
                self.IMG = self.IMG_TUPLE[0]
                self.idle = False
                self.double_jump_ready = False
                self.double_jump_done = True
                self.dY = self.F2

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
            self.double_jump_ready = False
            self.double_jump_done = False
            self.double_jump_counter = 0
            self.change_state('fall')

        if self.air:
            self.dY += self.G
            self.y += self.dY

    def double_jump_trigger_control(self):
        if self.air and not self.fall and not self.double_jump_done:
            self.double_jump_counter += 1
            if self.double_jump_counter >= self.DOUBLE_JUMP_LIMIT:
                self.double_jump_counter = 0
                self.double_jump_ready = True
                #print('DOUBLE_JUMP_LIMIT')

    # reset settings after landing on the ground or the pad
    def reset_settings(self):
        self.dY = 0
        self.air = False
        self.fall = False
        self.idle = False
        self.double_jump_ready = False
        self.double_jump_done = False
        self.double_jump_counter = 0
        self.change_state('idle')
