import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

# TODO load a background image


# a custom class that uses an image
from sprite_class import Sprite
# TODO create a Sprite object


# setup the font, other variables
my_font = pygame.font.Font('freesansbold.ttf', 12)
timer = 0
tick = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # reset the screen
    # screen.fill((255, 255, 255))
    # TODO


    # TODO draw the sprite
    


    # count ticks
    tick += 1
    # adjust timer & ticks
    if tick >= 250: # related to the delay value
        timer += 1
        tick = 0 # don't allow ticks to get too large
    
    # TODO draw the text



    # update the screen and pause
    pygame.display.update()
    pygame.time.delay(3)