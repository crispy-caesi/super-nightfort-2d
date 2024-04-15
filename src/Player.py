# ===================== import ===================== #

import pygame 
from MusicController import MusicController
# ===================== Player ===================== #

class Player(pygame.sprite.Sprite):
    """
    Class to handle the player and their attributes.
    """


    def __init__(self,__currentCharacterSkin):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(__currentCharacterSkin)
        self.rect = self.image.get_rect()
        # --- movement --- #
        self.__horizontalCollisionBox, self.__verticalCollisionBox = OffsetRect((255,255,0),self), OffsetRect((255,0,0),self)
        self.__isOnGround = False
        self.__acceleration = 0                 # acceleration of the player (force with which the player moves)
        self.__friction = -.05                  # deceleration to halt the player
        self.__gravity = 1                      # mass of the player
        self.__speed = pygame.math.Vector2(0,0) # speed of the player
        # --- health --- #
        self.__hurtMap = None
        self.__health = 3

        # --- animation --- #
        self.__image_index_run = 0
        self.__run_animation_index = 0

        self.__jumpImages = jumpImages
        self.__image_index_jump = 0
        self.__jump_animation_index = 0
        self.__jump_move_last_key = "right"


        self.__deathImages = deathImages
        self.__image_index_death = 0
        self.__death_animation_index = 0

        self.__isDead = False

        #music bzw. sounds
        self.__mcc = MusicController()
        self.__mcc.initJumpSound("sprites/placeholder/soundsAndMusic/Jump.wav")

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
            if self.__run_animation_index == 5:
                self.run_animation("left")
                self.__run_animation_index = 0

            self.__jump_move_last_key = "left"
            self.__run_animation_index += 1

        if __keyInput.keyright:
            self.__acceleration += .3
            if self.__run_animation_index == 5:
                self.run_animation("right")
                self.__run_animation_index = 0

            self.__run_animation_index += 1
            self.__jump_move_last_key = "right"


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
        #jump sound
        if __keyInput.keyspacePressed and self.__isOnGround:#play jump sound
            self.__mcc.playJumpSound()
            __keyInput.keyspacePressed = False

        # jump
        if __keyInput.keyspace:
            if self.__isOnGround:
                self.__speed.y -= 8
                self.__isOnGround = False
        
        # movement        
        self.__speed.y += self.__gravity

        if not(self.__speed.y > 0):
            #when I wrote this, only God and I understood what I was doing
            
            # This handles cases when both jumping and running are pressed simultaneously, 
            # and when only jumping is pressed, to ensure the player faces in the correct direction
            self.__jump_animation_index +=1  
            if self.__jump_animation_index == 4 :
                if __keyInput.keyleft:
                    self.jumpAnimation("left")
                    self.__jump_move_last_key = "left"

                elif __keyInput.keyright :
                    self.jumpAnimation("right")
                    self.__jump_move_last_key = "right"

                elif self.__jump_move_last_key == "left":
                    self.jumpAnimation("left")
                    self.__jump_move_last_key = "left"

                elif self.__jump_move_last_key == "right": 
                    self.jumpAnimation("right")
                    self.__jump_move_last_key = "right"
                  
                self.__jump_animation_index = 0
                #now, God only knows


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

        if __tileMap.rect.y <= -50:
            # Since the player isn't moving visibly, but rather the tilemap is, 
            # the Rect position of the tilemap is simply checked against its position. 
            # Then, when the position, in this case -100, is reached, the player is considered dead.
            if self.__death_animation_index == 3:
                self.deathAnimation()
                self.__death_animation_index = 0
            
            if self.__image_index_death >= len(self.__deathImages):
                self.dead()

            self.__death_animation_index += 1

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
        """
        set __isDead true, so that the main menu can start
        """
        print("player is death")
        self.__isDead = True
    
    def getIsDead(self)->bool:
        return self.__isDead

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


# ===================== Animation ===================== #

    def run_animation(self, direction):
        """
        run animatio of the character, diffrent direction needs difrent animations
        """        
        if direction == "left" and self.__isOnGround:
            self.__image_index_run += 1
            self.image = self.__images[self.__image_index_run % len(self.__images)]# This line assigns the current image to be displayed from a list of images based on the index, ensuring it loops through the images if the index exceeds the length of the list
            self.image = pygame.transform.flip(self.image, True, False) #flip the player in the opposite direction when the player moves left
        elif direction == "right" and self.__isOnGround:
            self.__image_index_run += 1
            self.image = self.__images[self.__image_index_run % len(self.__images)]
            self.image = pygame.transform.flip(self.image, False, False)
    
    def deathAnimation(self):
        self.__image_index_death += 1
        self.image = self.__deathImages[self.__image_index_death % len(self.__deathImages)]     

    def jumpAnimation(self, direction):
        if direction == "left":
            self.__image_index_jump += 1
            self.image = self.__jumpImages[self.__image_index_jump % len(self.__jumpImages)] 
            self.image = pygame.transform.flip(self.image, True, False)
        elif direction == "right":
            self.__image_index_jump += 1
            self.image = self.__jumpImages[self.__image_index_jump % len(self.__jumpImages)] 
            self.image = pygame.transform.flip(self.image, False, False)

# ===================== Offsetrect ===================== #

class OffsetRect(pygame.sprite.Sprite):
    """
    Class that generates collision checkboxes for player movement, input: player.
    """

    def __init__(self,color, __player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((__player.rect.w-20, __player.rect.h), pygame.SRCALPHA)# To reduce the hitbox by 20 to ensure proper collision detection for the player despite the animations (and avoid situations like getting caught on the arms).
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.Mask((__player.rect.w-20, __player.rect.h), True)
        self.rect.centerx, self.rect.centery = __player.rect.centerx, __player.rect.centery
        self.__offset = pygame.Vector2(0, 0)
        #elf.image.fill(color=color) #Ability to color the offset rects for debugging purposes

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
