import pygame
from .constants import WHITE, BACKGROUND, WIDTH, HEIGHT, FLOOR
from .player import Player
#import random

class Game():
    def __init__(self, win):
        self.win = win
        self.player = None
        self.create_player()
        self.gameover = False

    def update(self):
        # player
        if self.player:
            self.player.gravity()
            self.check_boundaries()
            self.player.change_image()

    def render(self):
        # background
        self.win.fill(WHITE)
        self.win.blit(BACKGROUND, (0, 0))

        # floor
        for i in range(WIDTH//16):
            self.win.blit(FLOOR, (i*16, HEIGHT-32))

        # player
        if self.player:
            self.player.draw(self.win)

        pygame.display.update()

    def create_player(self):
        self.player = Player(WIDTH//2, HEIGHT-FLOOR.get_height()-16)

    def check_boundaries(self):
        # check player collision with the floor after falling due to gravity
        if self.player.y > HEIGHT-FLOOR.get_height()-16:
            self.player.y = HEIGHT-FLOOR.get_height()-16
            self.player.dY = 0
            self.player.air = False
            self.player.fall = False
            self.player.idle = False
            self.player.change_state('idle')
