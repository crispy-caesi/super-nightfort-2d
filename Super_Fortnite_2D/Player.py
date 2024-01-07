# ===================== import ===================== #

import pygame
from Input import KeyInput

# ===================== Player ===================== #

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/placeholder/Duck.png")
        self.rect = self.image.get_rect()
        self.isonground = False
        self.health = 3
        self.damagetaken = False
        self.dead = False
        self.gravity = 0.5
        self.speed = pygame.math.Vector2(0,0)
        self.velocity_y = 0  # Geschwindigkeit in der y-Richtung
                
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
                self.velocity_y =- 12
                self.isonground = False
                
    def verticalmovement(self):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

    def playerUpdate(self, input_):
        self.horizontalMovement(input_)
        self.verticalmovement()    