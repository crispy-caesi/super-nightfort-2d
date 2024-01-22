# ===================== import ===================== #

import pygame
from pygame.sprite import Group
from Input import KeyInput
# ===================== Player ===================== #

class Player(pygame.sprite.Sprite):
    """
    Class to handle the player and their attributes.
    """ 
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/placeholder/Duck.png")
        self.rect = self.image.get_rect()
        self.temprect = self.rect
        # --- movement --- #
        self.__isonground = False
        self.__acceleration = 0                 # acceleration of the player (force with which the player moves)
        self.__friction = -.05                  # deceleration to halt the player
        self.__gravity = 1                      # mass of the player
        self.__speed = pygame.math.Vector2(0,0) # speed of the player
        self.position = pygame.math.Vector2(0,0)
        # --- health --- #
        self.__health = 3
        self.__damagetaken = False
        
        self.rightBox = OffsetRect(self,xOffset=2, yOffset=-2, colorcode=(255,255,255))
        self.bottomBox = OffsetRect(self,xOffset=0, yOffset=2, colorcode=(255,0,255))

# ============== player movement ============== #

# ======= horizontal ======= #

    def horizontalMovement(self, keyinput, tilemaprect):
        """
        Method to handle horizontal movement of the player.
        """ 

        self.__acceleration = 0

        if keyinput.keyleft:
            self.__acceleration -= .3

        if keyinput.keyright:
            self.__acceleration += .3

        self.__speed.x += self.__acceleration               #   F = m * a  |  m = 1  -->  F = a
        self.__speed.x += self.__friction * self.__speed.x  #   a * µ = a

        if abs(self.__speed.x) < .1:
            self.__speed.x = 0

        self.maxHorizontalSpeed(4)
        self.horizontalCollisionCheck(tilemaprect)
        self.rect.x += self.__speed.x
            
    def maxHorizontalSpeed(self, maxspeed):
        """
        Method to limit the speed to an input value.
        """
        
        if self.__speed.x < 0:
            return max(self.__speed.x, -maxspeed)
        
        else:
            return min(self.__speed.x, maxspeed)

    def horizontalCollisionCheck(self, tilemaprect):
        """
        Method to handle horizontal collisions.
        """
        
        if pygame.sprite.collide_mask(self.rightBox, tilemaprect):
            if self.__speed.x > 0:
                while pygame.sprite.collide_mask(self.rightBox, tilemaprect):
                    break
                    self.__speed.x = -4
                    self.rect.x += self.__speed.x
                self.__speed.x = 0
                    

# ======= vertical ======= #

    def verticalMovement(self, keyinput, tilemaprect):
        """
        Method to handle vertical movement of the player.
        """
        
        # jump
        if keyinput.keyspace:
            if self.__isonground:
                self.__speed.y -= 8
                self.__isonground = False

        # movement        
        self.__speed.y += self.__gravity

        if self.__speed.y > 0:
            self.__speed.y += self.__friction * self.__speed.y * 2.5

        self.verticalCollisionCheck(tilemaprect)
        self.rect.y += self.__speed.y

    def verticalCollisionCheck(self, tilemaprect):
        """
        Method to handle vertical collisions.
        """
        if self.__isonground:
            self.__speed.y = 0
            self.rect.y += self.__speed.y
            self.bottomBox.update_position(player=self)
            return
        
        
        if pygame.sprite.collide_mask(self.bottomBox, tilemaprect):
            self.__isonground = True
            
# ======= update ======= #
  
    def playerUpdate(self, keyinput, tilemaprect):
        """
        Method to update all player related events.
        """
        
        self.horizontalMovement(keyinput, tilemaprect)
        self.verticalMovement(keyinput, tilemaprect)
    
        self.rightBox.setOffsetX(self.__speed.x)
        self.rightBox.setOffsetY(0)
        
        self.bottomBox.setOffsetX(0)
        self.bottomBox.setOffsetY(self.__speed.y)
 
        self.rightBox.update_position(player=self)
        self.bottomBox.update_position(player=self)

# ============== damage and health ============== #

    def damage(self):
        """
        ouch.
        """
        
        if self.__damagetaken is True:
            self.__health -= 1
            self.__damagetaken = False

        if self.__health < 1:
            self.dead()

    def dead(self):
        """
        you died!
        """
        
        pass
    #TODO back to main menu and delete level stats in cache for the leaderboard

class OffsetRect(pygame.sprite.Sprite):
    def __init__(self, player: Player, xOffset, yOffset, colorcode):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 16))  # Pygame.SRCALPHA für eine transparente Oberfläche
        self.image.fill(colorcode)
        self.rect = self.image.get_rect()
                
        self.rect.centerx = player.rect.centerx + xOffset
        self.rect.centery = player.rect.centery + yOffset
        
        self.offset = pygame.Vector2()
    
    def setOffsetX(self, x):
        self.offset.x = x
    
    def setOffsetY(self, y):
        self.offset.y = y
        
    def getOffset(self):
        return self.offset
        
    def update_position(self, player: Player):
        self.rect.centerx = player.rect.centerx + self.getOffset().x
        self.rect.centery = player.rect.centery + self.getOffset().y 