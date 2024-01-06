# ===================== import ===================== #

import pygame
from Input import KeyInput

# ===================== Player Class ===================== #

class Player(pygame.sprite.Sprite):
    
    """
    class that creates the player and all their different properties
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/placeholder/Duck.png")
        self.rect = self.image.get_rect()
        self.maxvelocity = 6
        self.isonground = False
        self.health = 3
        self.damagetaken = False
        self.dead = False
        self.gravity = .01
        self.speed = pygame.math.Vector2(0,0)
    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

# ===================== Movement ===================== #

    def horizontalMovement(self, input_:KeyInput):
        self.speed.x = 0
        if input_.getkeyleft():
            self.speed.x = -4
        if input_.getkeyright():
           self.speed.x = 4
        self.rect.x += self.speed.x

    def jump(self, input_:KeyInput):
        if input_.getkeyspace():
            if self.isonground:
                self.speed.y += 8
                self.isonground = False
                
    def verticalmovement(self):
        self.speed.y += self.speed.y + self.gravity
        self.rect.y += self.speed.y

    def collisioncheck(self):
        pass
    '''
    TODO:
    Check collision with the tilemap
    if the collision is self.rect.y +- 16 (y axis with the player):
        reset self.speed.y to 0

    if the collision is self.rect.x +- 16 (x axis with the player):
        reset self.speed.x to 0
    
    if the collision is below the player:
        self.isonground = True    
    '''

    def playerupdate(self, input_:KeyInput):
        self.horizontalMovement(input_)
        self.verticalmovement()
        #self.collisioncheck()

# ===================== Damage and health ===================== #

    def damage(self):
        if self.damagetaken is True:
            self.health -= 1
            self.damagetaken = False

        if self.health < 1:
            self.dead = True

    def dead(self):
        pass
    #TODO back to main menu and delete level stats in cache for the leaderboard