# ===================== import ===================== #

import pygame
import Input

# ===================== Player ===================== #

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/placeholder/Duck.png")
        self.position = pygame.Rect(0,0,16,16)
        self.speed = 0
        self.maxvelocity = 5
        self.isonground = False

    def draw(self, display):
        display.blit(self.image, (self.position.x, self.position.y))

    def horizontalmovement(self):
        if Input.getkeyleft() is True:
            self.speed = max(self.speed - 1, -self.maxvelocity)
        if Input.getkeyright() is True:
            self.speed = min(self.speed + 1, self.maxvelocity)
        self.speed *= .8
        self.position = pygame.Rect.move(self, self.position.x + self.speed, self.position.y)

    def Jump(self):
        if Input.getkeyspace() is True:
            if self.isonground is True:
                self.speed = 8
                self.isonground = False
                self.position = pygame.Rect.move(self, self.position.x, self.position.y + self.speed)
        