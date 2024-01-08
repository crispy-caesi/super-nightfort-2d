# ===================== import ===================== #

import pygame
from Input import KeyInput

# ===================== Player ===================== #

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/placeholder/Duck.png")
        self.rect = self.image.get_rect()
        self.__isonground = False
        self.__health = 3
        self.__damagetaken = False
        self.__isdead = False
        self.__gravity = 0.5
        self.__speed = pygame.math.Vector2(0,0)
        self.position = pygame.math.Vector2(0,0)
                
    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

# ===================== Movement ===================== #

    def horizontal_Movement(self, keyinput:KeyInput):
        self.__speed.x = 0
        if keyinput.getkeyleft():
            self.__speed.x = -4
        if keyinput.getkeyright():
            self.__speed.x = 4    
        self.rect.x += self.__speed.x
            
    def vertical_movement(self, keyinput:KeyInput):#jump
        if keyinput.getkeyspace():
            if self.__isonground:
                self.__speed.y -= 8
                self.__isonground = False
        self.__speed.y += self.__gravity
        self.rect.y += self.__speed.y

    def horizontal_collisioncheck(self, tilemaprect):
        if pygame.sprite.collide_mask(self, tilemaprect):
            if self.__speed.x < 0:
                while pygame.sprite.collide_mask(self, tilemaprect):
                    self.__speed.x = 4
                    self.rect.x += self.__speed.x
                self.__speed.x = 0
            if self.__speed.x > 0:
                while pygame.sprite.collide_mask(self, tilemaprect):
                    self.__speed.x = -4
                    self.rect.x += self.__speed.x
                self.__speed.x = 0


    def vertical_collisioncheck(self, tilemaprect):
        if pygame.sprite.collide_mask(self, tilemaprect):
            if self.__speed.y > 0:     
                self.__isonground = True
                self.__speed.y = 0
                self.__gravity = 0
            if self.__speed.y < 0:
                self.__speed.y = 0
                self.__gravity = 0
        else:
            self.__gravity = 0.5
            self.__isonground = False
            
                
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