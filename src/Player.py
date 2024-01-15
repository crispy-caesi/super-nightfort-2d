# ===================== import ===================== #

import pygame
from Input import KeyInput

# ===================== Player ===================== #

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/placeholder/Duck.png")
        self.rect = self.image.get_rect()
        
        # health related
        self.__health = 3
        self.__damagetaken = False
        self.__isdead = False

        # movement related
        self.__isonground = False
        self.__acceleration = 0                 # acceleration of the player (force with which the player moves)
        self.__friction = -.05                  # ground friction
        self.__gravity = 1                      # mass of the player
        self.__speed = pygame.math.Vector2(0,0) # speed of the player
        self.position = pygame.math.Vector2(0,0)
       
    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

# ============== player movement ============== #
        
# ======= horizontal movement ======= #

    def horizontal_Movement(self, keyinput:KeyInput):
        """
        calculation for momentum:
        character -> F=m*a (mass= 1)
        ground -> a*µ=a (friction)
        input -> acceleration
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

        self.maxspeed(4)

        # connecting the calculated speed to the actual character coordinates
        self.rect.x += self.__speed.x
            
    def maxspeed(self,maxspeed):
        if self.__speed.x < 0:
            return max(self.__speed.x, -maxspeed)
        else:
            return min(self.__speed.x, maxspeed)
        
# ======= vertical movement ======= #
        
    def vertical_movement(self, keyinput:KeyInput):
        # jump
        if keyinput.keyspace:
            if self.__isonground:
                self.__speed.y -= 12
                self.__isonground = False
        # actual movement
        self.__speed.y += self.__gravity
        self.rect.y += self.__speed.y

# ======= collisionchecks ======= #
        
    def horizontal_collisioncheck(self, tilemaprect):
        if pygame.sprite.collide_mask(self, tilemaprect) and not self.__isonground:
            if self.__speed.x < 0:
                self.rect.x += 1
            if self.__speed.x > 0:
                self.rect.x -= 1
            self.__speed.x = 0
            print("check")

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
            self.__gravity = 1
            self.__isonground = False
            
                
    def playerupdate(self, keyinput:KeyInput, tilemaprect):
        self.horizontal_Movement(keyinput)
        self.horizontal_collisioncheck(tilemaprect)        
        self.vertical_movement(keyinput)
        self.vertical_collisioncheck(tilemaprect)

        print(f"{self.__isonground}")


# ============== damage and health ============== #

    def damage(self):
        if self.__damagetaken is True:
            self.__health -= 1
            self.__damagetaken = False

        if self.__health < 1:
            self.__isdead = True

    def dead(self):
        pass
    #TODO back to main menu and delete level stats in cache for the leaderboard