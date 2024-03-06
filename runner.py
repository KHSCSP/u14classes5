import pygame, sys, random
from pygame.locals import QUIT
from bouncy_class import Bouncy
from bullet_class import Bullet

w = 800
h = 600
pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')

# define one player, a list of 'bullets'
p1 = Bouncy(size=20,col=(255,0,0))

# define a list of bullets
bullets = []

# define a list of enemies
enemies = []
for i in range(10):
    enemies.append(Bouncy(size=20))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # a bit slower keypress (not continuous)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(p1.x, p1.y))
                print(len(bullets))
    # -------- end event loop
    screen.fill((255,255,255))

    
    # move and draw player
    if pygame.MOUSEMOTION:
        p1.x, p1.y = pygame.mouse.get_pos()
    p1.draw(screen)

    # bullets - move and draw
    # iterate through copy!! (for removal from list)
    for b in bullets[:]:
        if b.y > 0:  
            b.move()
            b.draw(screen)
        else:
            bullets.remove(b)

    # enemies move and draw
    for e in enemies:
        e.move(screen)
        e.draw(screen)

    # check for collision
    for b in bullets[:]:
        if b.check_hit(enemies):
            bullets.remove(b)
                
    
    pygame.display.update()
    pygame.time.delay(5)