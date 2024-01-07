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

    def horizontal_Movement(self, keyinput:KeyInput):
        self.__speed.x = 0
        if keyinput.getkeyleft:
            self.__speed.x = max(self.__speed.x-4, -self.__maxspeed)
        if keyinput.getkeyright:
           self.__speed.x = min(self.__speed.x+4, self.__maxspeed)
        self.rect.x += self.__speed.x
            
    def vertical_movement(self, keyinput:KeyInput):
        if keyinput.getkeyspace:
            if self.__isonground:
                self.__speed.y += 8
                self.__isonground = False
        self.__speed.y += self.__speed.y + self.__gravity
        self.rect.y += self.__speed.y

    def horizontal_collisioncheck(self, tilemaprect):
        if pygame.sprite.collide_mask(self, tilemaprect):
            if self.__speed.x < 0:
                while pygame.sprite.collide_mask(self, tilemaprect):
                    self.__speed.x = 6
                    self.rect.x += self.__speed.x
                self.__speed.x = 0
            if self.__speed.x > 0:
                while pygame.sprite.collide_mask(self, tilemaprect):
                    self.__speed.x = -6
                    self.rect.x += self.__speed.x
                self.__speed.x = 0

    def vertical_collisioncheck(self, tilemaprect):
        if pygame.sprite.collide_mask(self, tilemaprect):
            if self.__speed.y < 0:
                while pygame.sprite.collide_mask(self, tilemaprect):
                    self.__speed.y = 6
                    self.rect.y += self.__speed.y
                self.__speed.y = 0
                self.__isonground = True
            if self.__speed.y > 0:
                while pygame.sprite.collide_mask(self, tilemaprect):
                    self.__speed.y = -6
                    self.rect.y += self.__speed.y
                self.__speed.y = 0

    def playerupdate(self, keyinput:KeyInput, tilemaprect):
        self.horizontal_Movement(keyinput)
        self.horizontal_collisioncheck(tilemaprect)
        self.vertical_movement(keyinput)
        self.vertical_collisioncheck(tilemaprect)

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