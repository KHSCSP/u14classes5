import pygame

class Sprite:
    def __init__(self, xp=0, yp=0, sizep=20):
        self.x = xp
        self.y = yp
        self.size = sizep
        self.pic = pygame.image.load("u14SOLNS/u14classes3SOLNprev/button.PNG")
        self.pic = pygame.transform.scale(self.pic, (self.size, self.size))


    def draw(self, screen):
        screen.blit(self.pic, (self.x, self.y))

