import pygame, random, math

class Bouncy:
    def __init__(self, x=100, y=100, size=10, col=None):
        self.x = x
        self.y = y
        self.size = size
        self.xV = random.randint(-2,2)
        self.yV = random.randint(-2,2)
        if col == None:
            self.color = Bouncy.rand_col()
        else:
            self.color = col

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
    

    def move(self, screen):
        w, h = screen.get_size()
        if self.x-self.size<0 or self.x+self.size>w:
            self.xV *= -1
        if self.y-self.size<0 or self.y+self.size>h:
            self.yV *= -1
        self.x += self.xV
        self.y += self.yV
    
    def rand_move(self, screen):
        w, h = screen.get_size()
        self.x = random.randint(0,w)
        self.y = random.randint(0,h)

    def tele_move(self, screen):
        w, h = screen.get_size()
        if self.x < 0:
            self.x = h
        elif self.x > h:
            self.x = 0
        if self.y < 0:
            self.y = w
        elif self.y > w:
            self.y = 0
        self.x += self.xV
        self.y += self.yV


    # a helper function
    # not a method because no instance will call this
    def rand_col():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return (r,g,b)