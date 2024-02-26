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

        # player steering trigger
        if not game.gameover:
            keys = pygame.key.get_pressed() # zwraca slownik z wartosciami typu bool
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                game.player.move('left')
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                game.player.move('right')
            else:
                game.player.change_state('idle')

        game.update()
        game.render()

    pygame.quit()

main()