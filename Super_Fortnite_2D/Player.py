# ===================== import ===================== #

import pygame
from Input import Input_

# ===================== Player ===================== #

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/placeholder/Duck.png")
        self.rect = self.image.get_rect()
        self.maxvelocity = 6
        self.isonground = False
        

    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def horizontalMovement(self, input_:Input_):
        speed = 0
        if input_.getkeyleft():
            speed = -4
        if input_.getkeyright():
           speed = 4
           
        self.rect.x += speed
           

    def jump(self, input_:Input_):
        if input_.getkeyspace():
            if self.isonground:
                speed = 8
                self.isonground = False
                self.position = pygame.Rect.move(self, self.position.x, self.position.y + speed)
        