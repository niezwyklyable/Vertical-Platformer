from pygame.image import load
#from pygame.transform import scale
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
