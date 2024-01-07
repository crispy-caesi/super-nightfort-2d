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
        self.__maxspeed = 6
        self.__isonground = False
        self.__health = 3
        self.__damagetaken = False
        self.__isdead = False
        self.__gravity = .01
        self.__speed = pygame.math.Vector2(0,0)

# ===================== daws the player ===================== #

    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

# ===================== Movement ===================== #

    def horizontalMovement(self, input_:KeyInput):
        self.__speed.x = 0
        if input_.getkeyleft:
            self.__speed.x = max(self.__speed.x-4, -self.__maxspeed)
        if input_.getkeyright:
           self.__speed.x = min(self.__speed.x+4, self.__maxspeed)
        self.rect.x += self.__speed.x

    def jump(self, input_:KeyInput):
        if input_.getkeyspace:
            if self.__isonground:
                self.__speed.y += 8
                self.__isonground = False
                
    def verticalmovement(self):
        self.__speed.y += self.__speed.y + self.__gravity
        self.rect.y += self.__speed.y

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
        if self.__damagetaken is True:
            self.__health -= 1
            self.__damagetaken = False

        if self.__health < 1:
            self.__isdead = True

    def dead(self):
        pass
    #TODO back to main menu and delete level stats in cache for the leaderboard