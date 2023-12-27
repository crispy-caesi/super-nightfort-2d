# ===================== import ===================== #

import pygame
from Input import Input_

# ===================== Player ===================== #

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/placeholder/Duck.png")
        self.position = pygame.Rect(0,0,16,16)
        self.maxvelocity = 6
        self.isonground = False
        self.rect = self.image.get_rect()

    def draw(self, display):
        display.blit(self.image, (self.position.x, self.position.y))

    def horizontalMovement(self, input_:Input_):
        speed = 1
        if input_.getkeyleft():
             self.position.x -= speed
        if input_.getkeyright():
           self.position.x += speed
           

    def jump(self, input_:Input_):
        if input_.getkeyspace():
            if self.isonground:
                speed = 8
                self.isonground = False
                self.position = pygame.Rect.move(self, self.position.x, self.position.y + speed)
        