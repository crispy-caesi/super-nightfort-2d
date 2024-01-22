# ===================== import ===================== #

import pygame
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
        self.mask = pygame.mask.from_surface()
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
        
        if pygame.sprite.collide_mask(self, tilemaprect):

            if self.__speed.x > 0:
                self.__speed.x -= .1

            if self.__speed.x < 0:
                self.__speed.x += .1

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

        if pygame.sprite.collide_mask(self, tilemaprect):

            if self.__speed.y > 0:
                self.__speed.y -= 1

            if self.__speed.y < 0:
                self.__speed.y += 1

            self.__isonground = True

# ======= update ======= #
  
    def playerUpdate(self, keyinput, tilemaprect):
        """
        Method to update all player related events.
        """
        
        self.horizontalMovement(keyinput, tilemaprect)
        self.verticalMovement(keyinput, tilemaprect)

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
