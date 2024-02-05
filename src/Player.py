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
        # --- movement --- #
        self.__horizontalCollisionBox, self.__verticalCollisionBox = OffsetRect(self), OffsetRect(self)
        self.__isOnGround = False
        self.__acceleration = 0                 # acceleration of the player (force with which the player moves)
        self.__friction = -.05                  # deceleration to halt the player
        self.__gravity = 1                      # mass of the player
        self.__speed = pygame.math.Vector2(0,0) # speed of the player
        # --- health --- #
        self.__hurtMap = None
        self.__health = 3

    @property    
    def horizontalCollisionBox(self):
        return self.__verticalCollisionBox

    @property
    def verticalCollisionBox(self):
        return self.__horizontalCollisionBox

# ============== horizontal player movement ============== #

    def horizontalMovement(self, __keyInput, __tileMap):
        """
        Method to handle horizontal movement of the player.
        """ 

        self.__acceleration = 0

        if __keyInput.keyleft:
            self.__acceleration -= .3

        if __keyInput.keyright:
            self.__acceleration += .3

        self.__speed.x += self.__acceleration               #   F = m * a  |  m = 1  -->  F = a
        self.__speed.x += self.__friction * self.__speed.x  #   a * µ = a

        if abs(self.__speed.x) < .1:
            self.__speed.x = 0

        self.maxHorizontalSpeed(4)
        self.horizontalCollisionCheck(__tileMap)
        self.rect.x += self.__speed.x

    def maxHorizontalSpeed(self, __maxSpeed):
        """
        Method to limit the speed to an input value.
        """
        
        if self.__speed.x < 0:
            return max(self.__speed.x, -__maxSpeed)
        
        else:
            return min(self.__speed.x, __maxSpeed)

    def horizontalCollisionCheck(self, __tileMap):
        """
        Method to handle horizontal collisions.
        """

        if pygame.sprite.collide_mask(self.__verticalCollisionBox, __tileMap):

            if self.__speed.x > 0:

                while pygame.sprite.collide_mask(self.__verticalCollisionBox, __tileMap):
                    self.__speed.x = -1
                    self.rect.x += self.__speed.x
                    self.collisionBoxUpdate()

                self.__speed.x = 0

            if self.__speed.x < 0:

                while pygame.sprite.collide_mask(self.__verticalCollisionBox, __tileMap):

                    self.__speed.x = 1
                    self.rect.x += self.__speed.x
                    self.collisionBoxUpdate()

                self.__speed.x = 0

# ============== vertical player movement ============== #

    def verticalMovement(self, __keyInput, __tileMap):
        """
        Method to handle vertical movement of the player.
        """
        
        # jump
        if __keyInput.keyspace:
            if self.__isOnGround:
                self.__speed.y -= 8
                self.__isOnGround = False
        
        # movement        
        self.__speed.y += self.__gravity

        if self.__speed.y > 0:
            self.__speed.y += self.__friction * self.__speed.y * 2.5

        self.verticalCollisionCheck(__tileMap)
        self.rect.y += self.__speed.y

    def verticalCollisionCheck(self, __tileMap):
        """
        Method to handle vertical collisions.
        """

        if self.__isOnGround:
            self.__speed.y = 0
            self.rect.y += self.__speed.y
            self.collisionBoxUpdate()

            if not pygame.sprite.collide_mask(self.__horizontalCollisionBox, __tileMap):
                self.__isOnGround = False

            return
        
        if pygame.sprite.collide_mask(self.__horizontalCollisionBox, __tileMap):
            self.__isOnGround = True

# ============== update ============== #

    def playerUpdate(self, __keyInput, __tileMap, __hurtMapRect):
        """
        Method to update all player related events.
        """
        
        if self.__hurtMap is None:
            self.__hurtMap = __hurtMapRect

        self.horizontalMovement(__keyInput, __tileMap)
        self.verticalMovement(__keyInput, __tileMap)
        self.collisionBoxUpdate()

    def collisionBoxUpdate(self):
        """
        Method to update all collision related events.
        """
        
        self.__verticalCollisionBox.boxUpdate(self, self.__speed.x, -8)
        self.__horizontalCollisionBox.boxUpdate(self, 0, self.__speed.y + 3)

# ============== damage and health ============== #

    def dead(self):
        pass

    def environmentalHurtCheck(self):
        for damagingObjects in self.__hurtMap:
            if self.rect.colliderect(damagingObjects):
                self.__isHurt = True
                
        if self.__isHurt:
            self.dead()
    
    def enemyHurtCheck(self):
        for enemy in self.__enemies:
            if self.rect.colliderect(enemy):
                self.__health -= 1
                # ui health reduction
                # enemy removal
        
        if self.__health < 1:
            self.dead()

# ===================== Offsetrect ===================== #

class OffsetRect(pygame.sprite.Sprite):
    """
    Class that generates collision checkboxes for player movement, input: player.
    """

    def __init__(self, __player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((__player.rect.w, __player.rect.h), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.Mask((__player.rect.w, __player.rect.h), True)
        self.rect.centerx, self.rect.centery = __player.rect.centerx, __player.rect.centery
        self.__offset = pygame.Vector2(0, 0)

    def setOffset(self, __x, __y):
        """
        Setter for box offset.
        """
        
        self.__offset.x, self.__offset.y = __x, __y

    def updatePosition(self, __player):
        """
        Method to sync the collisionbox position to the current player position.
        """

        self.rect.centerx, self.rect.centery = (__player.rect.centerx + self.__offset.x), (__player.rect.centery + self.__offset.y) 

    def boxUpdate(self, __player, __x, __y):
        """
        Method to update all collision box attributes.
        """
        
        self.setOffset(__x, __y)
        self.updatePosition(__player)
