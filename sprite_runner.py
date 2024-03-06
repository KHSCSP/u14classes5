import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

# load a background image
bg = pygame.image.load("u14SOLNS/u14classes3SOLNprev/lighting.jpg")

# a custom class that uses an image
from sprite_class import Sprite
s = Sprite(50, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # reset the screen
    # screen.fill((255, 255, 255))
    screen.blit(bg, (0,0))

    # draw the sprite
    s.draw(screen)

    # update the screen and pause
    pygame.display.update()
    pygame.time.delay(3)