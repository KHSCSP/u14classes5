import pygame, sys, random
from pygame.locals import QUIT
from bouncy_class import Bouncy
from laser_class import Laser

w = 800
h = 600
pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')

# define one player


# define a list of lasers


# define a list of enemies



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # a bit slower keypress (not continuous)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
    # -------- end event loop
    screen.fill((255,255,255))

    
    # move and draw player



    # lasers - move and draw
    # iterate through copy!! (for removal from list)



    # enemies move and draw



    # check for collision


                
    
    pygame.display.update()
    pygame.time.delay(5)