from pygame.image import load
from pygame.transform import scale
from pygame.transform import flip

# screen refreshing frequency
FPS = 60

# screen dims
WIDTH, HEIGHT = 400, 600

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# background
BACKGROUND = load('assets/backgrounds/bg.png') # 400x600px

# ground
TERRAIN = load('assets/misc/Terrain/Terrain.png')
FLOOR = TERRAIN.subsurface(7*16, 0, 16, 32)

# player - idle state
PLAYER_IDLE_RIGHT = load('assets/player/Idle (32x32).png')
PLAYER_IDLE_LEFT = flip(PLAYER_IDLE_RIGHT, True, False) # mirroring player assets but changing their order
PLAYER_IDLE_RIGHT_LIST = []
for i in range(11):
    PLAYER_IDLE_RIGHT_LIST.append(PLAYER_IDLE_RIGHT.subsurface(i*32, 0, 32, 32))

PLAYER_IDLE_LEFT_LIST = []
for i in range(11):
    PLAYER_IDLE_LEFT_LIST.append(PLAYER_IDLE_LEFT.subsurface(i*32, 0, 32, 32))
PLAYER_IDLE_LEFT_LIST.reverse() # reorder assets to original order

# player - run state
PLAYER_RUN_RIGHT = load('assets/player/Run (32x32).png')
PLAYER_RUN_LEFT = flip(PLAYER_RUN_RIGHT, True, False) # mirroring player assets but changing their order
PLAYER_RUN_RIGHT_LIST = []
for i in range(12):
    PLAYER_RUN_RIGHT_LIST.append(PLAYER_RUN_RIGHT.subsurface(i*32, 0, 32, 32))

PLAYER_RUN_LEFT_LIST = []
for i in range(12):
    PLAYER_RUN_LEFT_LIST.append(PLAYER_RUN_LEFT.subsurface(i*32, 0, 32, 32))
PLAYER_RUN_LEFT_LIST.reverse() # reorder assets to original order

# player - air state
PLAYER_JUMP_RIGHT = load('assets/player/Jump (32x32).png')
PLAYER_JUMP_LEFT = flip(PLAYER_JUMP_RIGHT, True, False)
PLAYER_JUMP_RIGHT_LIST = [PLAYER_JUMP_RIGHT]
PLAYER_JUMP_LEFT_LIST = [PLAYER_JUMP_LEFT]

PLAYER_FALL_RIGHT = load('assets/player/Fall (32x32).png')
PLAYER_FALL_LEFT = flip(PLAYER_FALL_RIGHT, True, False)
PLAYER_FALL_RIGHT_LIST = [PLAYER_FALL_RIGHT]
PLAYER_FALL_LEFT_LIST = [PLAYER_FALL_LEFT]

PLAYER_DOUBLE_JUMP_RIGHT = load('assets/player/Double Jump (32x32).png')
PLAYER_DOUBLE_JUMP_LEFT = flip(PLAYER_DOUBLE_JUMP_RIGHT, True, False)
PLAYER_DOUBLE_JUMP_RIGHT_LIST = []
for i in range(6):
    PLAYER_DOUBLE_JUMP_RIGHT_LIST.append(PLAYER_DOUBLE_JUMP_RIGHT.subsurface(i*32, 0, 32, 32))

PLAYER_DOUBLE_JUMP_LEFT_LIST = []
for i in range(6):
    PLAYER_DOUBLE_JUMP_LEFT_LIST.append(PLAYER_DOUBLE_JUMP_LEFT.subsurface(i*32, 0, 32, 32))
PLAYER_DOUBLE_JUMP_LEFT_LIST.reverse() # reorder assets to original order

# pads
STEEL_PAD = scale(load('assets/pads/Pad_01_1.png'), (100, 20))
STEEL_PAD_LIST = [STEEL_PAD]
WOODEN_PAD = scale(load('assets/pads/Pad_02_1.png'), (100, 20))
WOODEN_PAD_LIST = [WOODEN_PAD]
MEADOW_PAD = scale(load('assets/pads/Pad_04_1.png'), (100, 20))
MEADOW_PAD_LIST = [MEADOW_PAD]
VOLCANIC_PAD = scale(load('assets/pads/Pad_03_1.png'), (100, 20))
VOLCANIC_PAD_LIST = [VOLCANIC_PAD]

# game settings
LEVEL_2_CHECKPOINT = 2000
LEVEL_3_CHECKPOINT = 4000
LEVEL_4_CHECKPOINT = 6000
GAME_OVER_CHECKPOINT = 8000
