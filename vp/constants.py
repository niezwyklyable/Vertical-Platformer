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

# game settings
LEVEL_2_CHECKPOINT = 2000
LEVEL_3_CHECKPOINT = 4000
LEVEL_4_CHECKPOINT = 6000
GAME_OVER_CHECKPOINT = 8000
TRAP_PERCENTAGE = 30 # probability of generating the trap instead of a pad
ENEMY_PERCENTAGE = 30 # probability of generating an enemy just above the pad
DIM_FACTOR = 0.8 # it decreases the base distance for collision detection method to make it more realistic and precisely
REPLICATE_FACTOR = 2 # it extends the lifetime of a single animation (positive int only)
DECAY_REPLICATE_FACTOR = 2 # like above but it concerns only player's decaying process (positive int only)
DECAY_LOOP_FACTOR = 6 # determines how many loops continue during decaying process (positive int only)

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

# player - hit state
PLAYER_HIT_RIGHT = load('assets/player/Hit (32x32).png')
PLAYER_HIT_LEFT = flip(PLAYER_HIT_RIGHT, True, False) # mirroring player assets but changing their order
PLAYER_HIT_RIGHT_LIST = []
for i in range(7):
    for _ in range(DECAY_REPLICATE_FACTOR):
        PLAYER_HIT_RIGHT_LIST.append(PLAYER_HIT_RIGHT.subsurface(i*32, 0, 32, 32))

PLAYER_HIT_LEFT_LIST = []
for i in range(7):
    for _ in range(DECAY_REPLICATE_FACTOR):
        PLAYER_HIT_LEFT_LIST.append(PLAYER_HIT_LEFT.subsurface(i*32, 0, 32, 32))
PLAYER_HIT_LEFT_LIST.reverse() # reorder assets to original order

# pads
STEEL_PAD = scale(load('assets/pads/Pad_01_1.png'), (100, 20))
STEEL_PAD_LIST = [STEEL_PAD]
WOODEN_PAD = scale(load('assets/pads/Pad_02_1.png'), (100, 20))
WOODEN_PAD_LIST = [WOODEN_PAD]
MEADOW_PAD = scale(load('assets/pads/Pad_04_1.png'), (100, 20))
MEADOW_PAD_LIST = [MEADOW_PAD]
VOLCANIC_PAD = scale(load('assets/pads/Pad_03_1.png'), (100, 20))
VOLCANIC_PAD_LIST = [VOLCANIC_PAD]

# traps
STEEL_TRAP = scale(load('assets/pads/Pad_01_2.png'), (100, 30))
STEEL_TRAP_LIST = [STEEL_TRAP]
WOODEN_TRAP = scale(load('assets/pads/Pad_02_2.png'), (100, 40))
WOODEN_TRAP_LIST = [WOODEN_TRAP]
MEADOW_TRAP = scale(load('assets/pads/Pad_04_2.png'), (100, 30))
MEADOW_TRAP_LIST = [MEADOW_TRAP]
VOLCANIC_TRAP = scale(load('assets/pads/Pad_03_2.png'), (100, 30))
VOLCANIC_TRAP_LIST = [VOLCANIC_TRAP]

# enemies
# bat
BAT_LEFT = load('assets/enemies/Bat/Flying (46x30).png')
BAT_RIGHT = flip(BAT_LEFT, True, False)
BAT_LEFT_LIST = []
for i in range(7):
    BAT_LEFT_LIST.append(BAT_LEFT.subsurface(i*46, 0, 46, 30))

BAT_RIGHT_LIST = []
for i in range(7):
    BAT_RIGHT_LIST.append(BAT_RIGHT.subsurface(i*46, 0, 46, 30))
BAT_RIGHT_LIST.reverse() # reorder assets to original order

# bird
BIRD_LEFT = load('assets/enemies/BlueBird/Flying (32x32).png')
BIRD_RIGHT = flip(BIRD_LEFT, True, False)
BIRD_LEFT_LIST = []
for i in range(9):
    BIRD_LEFT_LIST.append(BIRD_LEFT.subsurface(i*32, 0, 32, 32))

BIRD_RIGHT_LIST = []
for i in range(9):
    BIRD_RIGHT_LIST.append(BIRD_RIGHT.subsurface(i*32, 0, 32, 32))
BIRD_RIGHT_LIST.reverse() # reorder assets to original order

# ghost
GHOST_LEFT = load('assets/enemies/Ghost/Idle (44x30).png')
GHOST_RIGHT = flip(GHOST_LEFT, True, False)
GHOST_LEFT_LIST = []
for i in range(10):
    for _ in range(REPLICATE_FACTOR):
        GHOST_LEFT_LIST.append(GHOST_LEFT.subsurface(i*44, 0, 44, 30))

GHOST_RIGHT_LIST = []
for i in range(10):
    for _ in range(REPLICATE_FACTOR):
        GHOST_RIGHT_LIST.append(GHOST_RIGHT.subsurface(i*44, 0, 44, 30))
GHOST_RIGHT_LIST.reverse() # reorder assets to original order

# skull
SKULL_RIGHT = load('assets/enemies/Skull/Idle 1 (52x54).png')
SKULL_LEFT = flip(SKULL_RIGHT, True, False)
SKULL_RIGHT_LIST = []
for i in range(8):
    for _ in range(REPLICATE_FACTOR):
        SKULL_RIGHT_LIST.append(scale(SKULL_RIGHT.subsurface(i*52, 0, 52, 54), (32, 34)))

SKULL_LEFT_LIST = []
for i in range(8):
    for _ in range(REPLICATE_FACTOR):
        SKULL_LEFT_LIST.append(scale(SKULL_LEFT.subsurface(i*52, 0, 52, 54), (32, 34)))
SKULL_LEFT_LIST.reverse() # reorder assets to original order
