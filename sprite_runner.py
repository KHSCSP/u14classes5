import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

# load a background image
bg = pygame.image.load("u14/u14classes5/lighting.jpg")

# a custom class that uses an image
from sprite_class import Sprite
s = Sprite(50, 50, 50)

# setup the font
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
    screen.blit(bg, (0,0))

    # draw the sprite
    s.draw(screen)


    # count ticks
    tick += 1
    # adjust timer & ticks
    if tick >= 250: # related to the delay value
        timer += 1
        tick = 0 # don't allow ticks to get too large
    # draw the text
    text = my_font.render('Time: ' + str(timer), True, (0,0,0))
    screen.blit(text, (0,0))

    # update the screen and pause
    pygame.display.update()
    pygame.time.delay(3)