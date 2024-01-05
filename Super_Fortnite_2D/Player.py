# ===================== import ===================== #

import pygame
from Input import KeyInput

# ===================== Player ===================== #

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/placeholder/Duck.png")
        self.rect = self.image.get_rect()
        self.maxvelocity = 6
        self.isonground = False
        self.health = 3
        self.damagetaken = False
        self.dead = False
        self.gravity = .04
        self.speed = pygame.math.Vector2(0,0)
    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def horizontalMovement(self, input_:KeyInput):
        self.speed.x = 0
        if input_.getkeyleft():
            self.speed.x = -4
        if input_.getkeyright():
           self.speed.x = 4
        self.rect.x += self.speed.x
    
    def damage(self):
        if self.damagetaken is True:
            self.health -= 1
        if self.health == 0:
            self.dead = True


    def jump(self, input_:KeyInput):
        if input_.getkeyspace():
            if self.isonground:
                self.speed.y += 8
                self.isonground = False
                
    def verticalmovement(self):
        self.speed.y += self.speed.y + self.gravity
        self.rect.y += self.speed.y

    def playerupdate(self, input_:KeyInput):
        self.horizontalMovement(self, input_)
        self.verticalmovement(self)