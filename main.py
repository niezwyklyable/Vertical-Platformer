import pygame
from vp.constants import WIDTH, HEIGHT, FPS
from vp.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Vertical Platformer by AW')

def main():
    # main settings
    clock = pygame.time.Clock()
    run = True
    #pygame.init() # it is needed for font module initialization
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)

        game.update()
        game.render()

    pygame.quit()

main()