import pygame
from .constants import WHITE, BACKGROUND, WIDTH, HEIGHT, FLOOR
from .player import Player
from .pad import Pad
#import random

class Game():
    def __init__(self, win):
        self.win = win
        self.player = None
        self.pads = []
        self.create_player()
        self.create_pads()
        self.gameover = False
        self.exceed = False # if player exceeds the half of the screen then it goes True until screen completes moving
        self.delta_y = 1 # y step of screen movement animation (possibly its value can be changed in the future so it is not a const)
        self.floor_y = HEIGHT-32 # y of the floor
        self.bg1_y = 0 # y of the first background
        self.bg2_y = -BACKGROUND.get_height() # y of the next background

    def update(self):
        # player
        if self.player:
            self.player.double_jump_trigger_control()
            self.player.gravity()
            self.check_boundaries()
            
            # collisions with pads
            if self.player.fall:
                for p in self.pads:
                    if self.collision_detection(self.player, p):
                        self.player.reset_settings()
                        p.landed = True
                        break
            if not self.player.air:
                for p in self.pads:
                    if p.landed:
                        if self.player.x > p.x + p.IMG.get_width()//2 \
                        or self.player.x < p.x - p.IMG.get_width()//2:
                            self.player.dY = 0.01 # some positive and small value to activate gravity method
                            break
            if self.player.air:
                for p in self.pads:
                    if p.landed:
                        p.landed = False # clear the flag if player jumps from this specific pad
                        break

            self.player.change_image()

            # screen movement (actually it is not the screen to move but all the objects)
            if self.player.y < HEIGHT//2: #and not self.exceed:
                self.exceed = True
            if self.exceed:
                self.screen_movement_control()

    def render(self):
        # background
        self.win.fill(WHITE)
        self.win.blit(BACKGROUND, (0, self.bg1_y))
        self.win.blit(BACKGROUND, (0, self.bg2_y))
        if self.bg1_y >= HEIGHT:
            self.bg1_y = -BACKGROUND.get_height()
        if self.bg2_y >= HEIGHT:
            self.bg2_y = -BACKGROUND.get_height()

        # floor
        for i in range(WIDTH//16):
            self.win.blit(FLOOR, (i*16, self.floor_y))

        # pads
        for p in self.pads:
            p.draw(self.win)

        # player
        if self.player:
            self.player.draw(self.win)

        pygame.display.update()

    def create_player(self):
        self.player = Player(WIDTH//2, HEIGHT-FLOOR.get_height()-16)

    def create_pads(self):
        self.pads.append(Pad(150, 400))
        self.pads.append(Pad(300, 150))
        self.pads.append(Pad(150, -100))
        self.pads.append(Pad(300, -350))

    def check_boundaries(self):
        # check player collision with the floor after falling due to gravity
        if self.floor_y < HEIGHT: # first check if floor is visible on the screen
            if self.player.y > self.floor_y-16:
                self.player.y = self.floor_y-16
                self.player.reset_settings()

    def collision_detection(self, obj1, obj2):      
        if obj1.TYPE == 'PLAYER' and obj2.TYPE == 'PAD':
            if obj1.y + obj1.IMG.get_height()//2 > obj2.y - obj2.IMG.get_height()//2 \
                and obj1.x > obj2.x - obj2.IMG.get_width()//2 \
                and obj1.x < obj2.x + obj2.IMG.get_width()//2 \
                and obj1.y + obj1.IMG.get_height()//2 < obj2.y + obj2.IMG.get_height()//2:
                obj1.y = obj2.y - obj2.IMG.get_height()//2 - obj1.IMG.get_height()//2
                return True
            
        return False
    
    def screen_movement_control(self):
        if self.player.y < HEIGHT//2:
            self.bg1_y += self.delta_y
            self.bg2_y += self.delta_y
            self.floor_y += self.delta_y
            for p in self.pads:
                p.y += self.delta_y
            self.player.y += self.delta_y
        else:
            self.exceed = False
