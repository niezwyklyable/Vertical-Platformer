from .sprite import Sprite
from .constants import TRAMPOLINE_IDLE_LIST, TRAMPOLINE_JUMP_LIST

class Trampoline(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=TRAMPOLINE_IDLE_LIST, TYPE='TRAMPOLINE', x=x, y=y)
        self.idle = True
        