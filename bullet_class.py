import pygame, math

class Bullet:
    def __init__(self, xp, yp):
        self.x = xp
        self.y = yp
        self.size = 5
        self.yv = -3
        self.color = (0,0,0)
    
    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x, self.y+self.size))

    def move(self):
        self.y += self.yv

    def check_hit(self, enemies):
        for e in enemies[:]:
            dist = math.sqrt((self.x-e.x)**2 + (self.y-e.y)**2)
            if dist <= e.size:
                enemies.remove(e)
                return True
        return False