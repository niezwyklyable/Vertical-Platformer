import pygame
from .constants import WHITE, BACKGROUND, WIDTH, HEIGHT, FLOOR
#import random

class Game():
    def __init__(self, win):
        self.win = win

    def update(self):
        pass

    def render(self):
        # background
        self.win.fill(WHITE)
        self.win.blit(BACKGROUND, (0, 0))

        # floor
        for i in range(WIDTH//16):
            self.win.blit(FLOOR, (i*16, HEIGHT-32))

        pygame.display.update()
