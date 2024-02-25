from pygame.image import load
#from pygame.transform import scale

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

# player
PLAYER_IDLE = load('assets/player/Idle (32x32).png')
PLAYER_IDLE_LIST = []
for i in range(11):
    PLAYER_IDLE_LIST.append(PLAYER_IDLE.subsurface(i*32, 0, 32, 32))
