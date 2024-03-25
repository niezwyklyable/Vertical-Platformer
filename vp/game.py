import pygame
from .constants import WHITE, BACKGROUND, WIDTH, HEIGHT, FLOOR, GAME_OVER_CHECKPOINT, \
TRAP_PERCENTAGE, LEVEL_2_CHECKPOINT, LEVEL_3_CHECKPOINT, LEVEL_4_CHECKPOINT, \
ENEMY_PERCENTAGE, DIM_FACTOR
from .player import Player
from .pad import Pad
import random
from .enemies import Enemy

class Game():
    def __init__(self, win):
        self.win = win
        self.player = None
        self.pads = []
        self.enemies = []
        self.create_player()
        self.screen_counter = 0 # number of screens that player passed (it is necessary to determine altitude for the next generated pads)
        self.PAD_SPACE = 100 # y distance between two nearest pads
        self.create_pads()
        self.gameover = False
        self.delta_y = 2 # y step of screen movement animation when player progresses upwards (possibly its value can be changed in the future so it is not a const)
        self.inactive_delta_y = 0.5 # y step of screen movement animation when player does not progress upwards - should be not lesser than above value (possibly its value can be changed in the future so it is not a const)
        self.floor_y = HEIGHT-32 # y of the floor
        self.bg1_y = 0 # y of the first background
        self.bg2_y = -BACKGROUND.get_height() # y of the next background
        self.score = 0

    def update(self):
        # player
        if self.player:
            if not self.gameover:
                self.player.double_jump_trigger_control()
                self.player.gravity()
                self.check_boundaries()
            
                # collisions with enemies
                for e in self.enemies:
                    if self.collision_detection(self.player, e):
                        self.gameover = True
                        self.player.decaying = True

            # collisions with pads
            if self.player.fall:
                for p in self.pads:
                    if self.collision_detection(self.player, p):
                        self.player.reset_settings()
                        p.landed = True
                        # score - max altitude measurement
                        if p.altitude > self.score:
                            self.score = p.altitude
                            if self.score == GAME_OVER_CHECKPOINT:
                                self.gameover = True
                                print('YOU WON !!! GAME OVER !!!')
                            print(f'SCORE: {self.score}')
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

            # animations
            if self.player.decaying:
                if self.player.decay():
                    pass # do nothing - let objects animate until it finishes
                else:
                    print(f'YOU LOST !!! GAMEOVER !!!')
                    print(f'SCORE: {self.score}')
                    self.player.decaying = False
            elif not self.gameover:
                self.player.change_image()
            else:
                self.player = None
                return

            # screen movement (actually it is not the screen to move but all the objects)
            self.screen_movement_control()

        # enemies
        for e in self.enemies:
            e.move()
            e.change_image()

    def render(self):
        # background
        self.win.fill(WHITE)
        self.win.blit(BACKGROUND, (0, self.bg1_y))
        self.win.blit(BACKGROUND, (0, self.bg2_y))
        if self.bg1_y >= HEIGHT:
            self.bg1_y = -BACKGROUND.get_height()
            self.create_pads() # create_pads() method trigger
        if self.bg2_y >= HEIGHT:
            self.bg2_y = -BACKGROUND.get_height()
            self.create_pads() # create_pads() method trigger

        # floor
        for i in range(WIDTH//16):
            self.win.blit(FLOOR, (i*16, self.floor_y))

        # pads
        for p in self.pads:
            p.draw(self.win)

        # enemies
        for e in self.enemies:
            e.draw(self.win)

        # player
        if self.player:
            self.player.draw(self.win)

        pygame.display.update()

    def create_player(self):
        self.player = Player(WIDTH//2, HEIGHT-FLOOR.get_height()-16)

    def create_pads(self):
        altitude = self.screen_counter * HEIGHT
        # the first two screens of pads who appear immediately when the game starts
        if altitude == 0:
            for y in range(HEIGHT, -HEIGHT, -self.PAD_SPACE):
                w = random.choice(range(80, 130, 10))
                # check if it can generate a trap instead of a regular pad
                trap_chance = random.choice(range(100))
                if trap_chance <= TRAP_PERCENTAGE and \
                    altitude + HEIGHT - y + self.PAD_SPACE != LEVEL_2_CHECKPOINT and \
                    altitude + HEIGHT - y + self.PAD_SPACE != LEVEL_3_CHECKPOINT and \
                    altitude + HEIGHT - y + self.PAD_SPACE != LEVEL_4_CHECKPOINT and \
                    altitude + HEIGHT - y + self.PAD_SPACE != GAME_OVER_CHECKPOINT:
                    # protection from generating two traps in a row and a first pad as a trap
                    if self.pads:
                        if not self.pads[-1].trap:
                            trap = True
                        else:
                            trap = False
                    else:
                        trap = False
                else:
                    trap = False
                self.pads.append(Pad(random.choice(range(w//2, WIDTH-w//2, 10)), \
                                    y - self.PAD_SPACE, \
                                    w, \
                                    altitude + HEIGHT - y + self.PAD_SPACE, \
                                    trap))
            self.create_enemies()
            self.screen_counter = 2
        # generate the next screen of pads
        else:
            for y in range(0, -HEIGHT, -self.PAD_SPACE):
                if altitude - y + self.PAD_SPACE > GAME_OVER_CHECKPOINT:
                    break
                w = random.choice(range(80, 130, 10))
                # check if it can generate a trap instead of a regular pad
                trap_chance = random.choice(range(100))
                if trap_chance <= TRAP_PERCENTAGE and \
                    altitude - y + self.PAD_SPACE != LEVEL_2_CHECKPOINT and \
                    altitude - y + self.PAD_SPACE != LEVEL_3_CHECKPOINT and \
                    altitude - y + self.PAD_SPACE != LEVEL_4_CHECKPOINT and \
                    altitude - y + self.PAD_SPACE != GAME_OVER_CHECKPOINT:
                    # protection from generating two traps in a row and a first pad as a trap
                    if self.pads:
                        if not self.pads[-1].trap:
                            trap = True
                        else:
                            trap = False
                    else:
                        trap = False
                else:
                    trap = False
                self.pads.append(Pad(random.choice(range(w//2, WIDTH-w//2, 10)), \
                                    y - self.PAD_SPACE, \
                                    w, \
                                    altitude - y + self.PAD_SPACE, \
                                    trap))
            self.create_enemies()
            self.screen_counter += 1

    def create_enemies(self):
        altitude = self.screen_counter * HEIGHT
        # the first two screens of enemies who appear immediately when the game starts
        if altitude == 0:
            for y in range(HEIGHT, -HEIGHT, -self.PAD_SPACE):
                # check the chance to generate an enemy
                enemy_chance = random.choice(range(100))
                if enemy_chance <= ENEMY_PERCENTAGE and \
                    altitude + HEIGHT - y + self.PAD_SPACE != LEVEL_2_CHECKPOINT and \
                    altitude + HEIGHT - y + self.PAD_SPACE != LEVEL_3_CHECKPOINT and \
                    altitude + HEIGHT - y + self.PAD_SPACE != LEVEL_4_CHECKPOINT and \
                    altitude + HEIGHT - y + self.PAD_SPACE != GAME_OVER_CHECKPOINT:
                    # protection from generating two enemies in a row and above the first pad
                    if y < HEIGHT:
                        if self.enemies:
                            if altitude + HEIGHT - y + self.PAD_SPACE - self.enemies[-1].altitude > self.PAD_SPACE:
                                enemy = True
                            else:
                                enemy = False
                        else:
                            enemy = True
                    else:
                        enemy = False
                else:
                    enemy = False
                if enemy:
                    self.enemies.append(Enemy(random.choice(range(56//2, WIDTH-56//2, 10)), \
                                        y - self.PAD_SPACE - 64//2, \
                                        random.choice(('right', 'left')), \
                                        altitude + HEIGHT - y + self.PAD_SPACE))
        # generate the next screen of enemies
        else:
            for y in range(0, -HEIGHT, -self.PAD_SPACE):
                if altitude - y + self.PAD_SPACE > GAME_OVER_CHECKPOINT:
                    break
                # check the chance to generate an enemy
                enemy_chance = random.choice(range(100))
                if enemy_chance <= ENEMY_PERCENTAGE and \
                    altitude - y + self.PAD_SPACE != LEVEL_2_CHECKPOINT and \
                    altitude - y + self.PAD_SPACE != LEVEL_3_CHECKPOINT and \
                    altitude - y + self.PAD_SPACE != LEVEL_4_CHECKPOINT and \
                    altitude - y + self.PAD_SPACE != GAME_OVER_CHECKPOINT:
                    # protection from generating two enemies in a row and above the first pad
                    if y < 0:
                        if self.enemies:
                            if altitude - y + self.PAD_SPACE - self.enemies[-1].altitude > self.PAD_SPACE:
                                enemy = True
                            else:
                                enemy = False
                        else:
                            enemy = True
                    else:
                        enemy = False
                else:
                    enemy = False
                if enemy:
                    self.enemies.append(Enemy(random.choice(range(56//2, WIDTH-56//2, 10)), \
                                        y - self.PAD_SPACE - 64//2, \
                                        random.choice(('right', 'left')), \
                                        altitude - y + self.PAD_SPACE))

    def check_boundaries(self):
        # check player collision with the floor after falling due to gravity
        if self.floor_y < HEIGHT: # first check if floor is visible on the screen
            if self.player.y > self.floor_y-16:
                self.player.y = self.floor_y-16
                self.player.reset_settings()
        else: # if not, it means that player could fell from the pad and be out of the screen
            if self.player.y > HEIGHT + self.player.IMG.get_height()//2:
                self.gameover = True
                print(f'YOU LOST !!! GAMEOVER !!!')
                print(f'SCORE: {self.score}')

    def collision_detection(self, obj1, obj2):      
        if obj1.TYPE == 'PLAYER' and obj2.TYPE == 'PAD':
            if obj1.y + obj1.IMG.get_height()//2 > obj2.y - obj2.IMG.get_height()//2 \
                and obj1.x > obj2.x - obj2.IMG.get_width()//2 \
                and obj1.x < obj2.x + obj2.IMG.get_width()//2 \
                and obj1.y + obj1.IMG.get_height()//2 < obj2.y + obj2.IMG.get_height()//2:
                obj1.y = obj2.y - obj2.IMG.get_height()//2 - obj1.IMG.get_height()//2
                return True
            
        if obj1.TYPE == 'PLAYER' and obj2.TYPE == 'ENEMY':
            # check distances between positions of two objects in a range of both objects
            if abs(obj1.x - obj2.x) <= (obj1.IMG.get_width()//2 + obj2.IMG.get_width()//2)*DIM_FACTOR and \
                abs(obj1.y - obj2.y) <= (obj1.IMG.get_height()//2 + obj2.IMG.get_height()//2)*DIM_FACTOR:
                return True

        return False
    
    def screen_movement_control(self):
        # when player progresses upwards
        if self.player.y < HEIGHT//2:
            self.bg1_y += self.delta_y
            self.bg2_y += self.delta_y
            self.floor_y += self.delta_y
            for p in self.pads:
                p.y += self.delta_y
            self.player.y += self.delta_y
            for e in self.enemies:
                e.y += self.delta_y
        # when player does not progresses upwards (stays inactive)
        elif self.floor_y >= HEIGHT and not self.gameover:
            self.bg1_y += self.inactive_delta_y
            self.bg2_y += self.inactive_delta_y
            self.floor_y += self.inactive_delta_y
            for p in self.pads:
                p.y += self.inactive_delta_y
            self.player.y += self.inactive_delta_y
            for e in self.enemies:
                e.y += self.inactive_delta_y
