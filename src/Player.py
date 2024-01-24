# ===================== import ===================== #

import pygame

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
        self.__horizontalCollisionBox = OffsetRect(self,xOffset=0, yOffset=2)
        self.__verticalCollisionBox = OffsetRect(self,xOffset=2, yOffset=-4)
        self.__isonground = False
        self.__acceleration = 0                 # acceleration of the player (force with which the player moves)
        self.__friction = -.05                  # deceleration to halt the player
        self.__gravity = 1                      # mass of the player
        self.__speed = pygame.math.Vector2(0,0) # speed of the player
        # --- health --- #
        self.__health = 3

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
        # repeat until the player's rightBox no longer touches anything
        if pygame.sprite.collide_mask(self.__verticalCollisionBox, tilemaprect):
            if self.__speed.x > 0:
                while pygame.sprite.collide_mask(self.__verticalCollisionBox, tilemaprect):
                    self.__speed.x = -1
                    self.rect.x += self.__speed.x
                    self.offsetsUpdates()
                self.__speed.x = 0
            if self.__speed.x < 0:
                while pygame.sprite.collide_mask(self.__verticalCollisionBox, tilemaprect):
                    self.__speed.x = 1
                    self.rect.x += self.__speed.x
                    self.offsetsUpdates()
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
            self.offsetsUpdates()
            if not pygame.sprite.collide_mask(self.__horizontalCollisionBox, tilemaprect):
                self.__isonground = False
            return
        
        
        if pygame.sprite.collide_mask(self.__horizontalCollisionBox, tilemaprect):
            self.__isonground = True
            
# ======= update ======= #

    def offsetsUpdates(self):
        """
        Method to update the collision box position
        """
        
        self.__verticalCollisionBox.setOffset(self.__speed.x, -8)
        self.__horizontalCollisionBox.setOffset(0, self.__speed.y + 3)
        self.__verticalCollisionBox.update_position(player=self)
        self.__horizontalCollisionBox.update_position(player=self)
  
    def playerUpdate(self, keyinput, tilemaprect):
        """
        Method to update all player related events.
        """
        
        self.horizontalMovement(keyinput, tilemaprect)
        self.verticalMovement(keyinput, tilemaprect)
        self.offsetsUpdates()

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
    

# --- getter for the collision boxes --- #
    @property    
    def horizontalCollisionBox(self):
        return self.__verticalCollisionBox
    
    @property
    def verticalCollisionBox(self):
        return self.__horizontalCollisionBox

class OffsetRect(pygame.sprite.Sprite):
    """
        Class that generates collision checkboxes for player movement

        Arguments:
            player (Player): used to access the player's positions.
            offset (float): x and y offset position  
    """
    
    def __init__(self, player: Player, xOffset, yOffset):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 16), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.Mask((16, 16), True)
        self.rect.centerx = player.rect.centerx + xOffset
        self.rect.centery = player.rect.centery + yOffset
        self.offset = pygame.Vector2(0, 0)

# --- getter and setter for the offset --- #    
    def setOffset(self, x, y):
        self.offset.x = x
        self.offset.y = y

    def update_position(self, player: Player):
        """
        Method to sync the collisionbox position to the current player position
        """

        self.rect.centerx = player.rect.centerx + self.offset.x
        self.rect.centery = player.rect.centery + self.offset.y 