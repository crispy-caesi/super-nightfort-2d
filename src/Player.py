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
        self.__horizontalCollisionBox, self.__verticalCollisionBox = OffsetRect(self), OffsetRect(self)
        self.__isonground = False
        self.__acceleration = 0                 # acceleration of the player (force with which the player moves)
        self.__friction = -.05                  # deceleration to halt the player
        self.__gravity = 1                      # mass of the player
        self.__speed = pygame.math.Vector2(0,0) # speed of the player
        # --- health --- #
        self.__health = 3

    @property    
    def horizontalCollisionBox(self):
        return self.__verticalCollisionBox

    @property
    def verticalCollisionBox(self):
        return self.__horizontalCollisionBox

# ============== horizontal player movement ============== #

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

        if pygame.sprite.collide_mask(self.__verticalCollisionBox, tilemaprect):

            if self.__speed.x > 0:

                while pygame.sprite.collide_mask(self.__verticalCollisionBox, tilemaprect):
                    self.__speed.x = -1
                    self.rect.x += self.__speed.x
                    self.collisionBoxUpdate()

                self.__speed.x = 0

            if self.__speed.x < 0:

                while pygame.sprite.collide_mask(self.__verticalCollisionBox, tilemaprect):

                    self.__speed.x = 1
                    self.rect.x += self.__speed.x
                    self.collisionBoxUpdate()

                self.__speed.x = 0

# ============== vertical player movement ============== #

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
            self.collisionBoxUpdate()

            if not pygame.sprite.collide_mask(self.__horizontalCollisionBox, tilemaprect):
                self.__isonground = False

            return
        
        if pygame.sprite.collide_mask(self.__horizontalCollisionBox, tilemaprect):
            self.__isonground = True

# ============== update ============== #

    def playerUpdate(self, keyinput, tilemaprect):
        """
        Method to update all player related events.
        """
        
        self.horizontalMovement(keyinput, tilemaprect)
        self.verticalMovement(keyinput, tilemaprect)
        self.collisionBoxUpdate()

    def collisionBoxUpdate(self):
        """
        Method to update all collision related events.
        """
        
        self.__verticalCollisionBox.boxUpdate(self, self.__speed.x, -8)
        self.__horizontalCollisionBox.boxUpdate(self, 0, self.__speed.y + 3)

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

# ===================== Offsetrect ===================== #

class OffsetRect(pygame.sprite.Sprite):
    """
    Class that generates collision checkboxes for player movement, input: player.
    """

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((player.rect.w, player.rect.h), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.Mask((player.rect.w, player.rect.h), True)
        self.rect.centerx, self.rect.centery = player.rect.centerx, player.rect.centery
        self.offset = pygame.Vector2(0, 0)

    def setOffset(self, x, y):
        """
        Setter for box offset.
        """
        
        self.offset.x, self.offset.y = x, y

    def updatePosition(self, player):
        """
        Method to sync the collisionbox position to the current player position.
        """

        self.rect.centerx, self.rect.centery = (player.rect.centerx + self.offset.x), (player.rect.centery + self.offset.y) 

    def boxUpdate(self, player, x, y):
        """
        Method to update all collision box attributes.
        """
        
        self.setOffset(x, y)
        self.updatePosition(player)
