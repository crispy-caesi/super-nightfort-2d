# ===================== import ===================== #

import pygame
import csv

# ===================== tile ===================== #

class Tile(pygame.sprite.Sprite):
    """
    Class to create a single tile.
    """

    def __init__(self, __image, __x, __y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(__image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = __x, __y

# ===================== tilemap ===================== #
        
class TileMap(pygame.sprite.Sprite):
    """
    Class to create the tilemap with which other objects can interact.
    """
    
    def __init__(self, __csvPath:str):
        super().__init__()
        self.__tiles = []    
        self.__hurtMap = [] 
        lst = self.readCSV( filePath = __csvPath)
        
        for column in range(len(lst)):
            for row in range(len(lst[0])):
                if lst[column][row] == "4": # player sprite
                   tile = Tile("sprites/placeholder/Duck.png", row * 16, column * 16)
                   self.__tiles.append(tile)
                if  lst[column][row] == "1":# gras
                   tile = Tile("sprites/placeholder/Grass.png", row * 16, column * 16)
                   self.__tiles.append(tile)
                if lst[column][row] == "2": # dirt
                   tile = Tile("sprites/placeholder/Dirt.png", row * 16, column * 16 )
                   self.__tiles.append(tile)
                if lst[column][row] == "5": # spikes
                   tile = Tile("sprites/placeholder/Dirt.png", row * 16, column * 16 )
                   self.__hurtMap.append(tile.rect)
                   self.__tiles.append(tile)

        __combined = Combined(self.__tiles)
        self.image = __combined.image
        self.rect = self.image.get_rect()
        
    def getHurtMap(self):
        return self.__hurtMap

    def updateTilemapPosition(self):
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y

    def readCSV(self, filePath:str)->list:
        __data = [[]]
        try:
            __file = open(filePath, "r")  
            __data = list(csv.reader(__file, delimiter=","))
            __file.close()
        except:
            print("Can't read csv file")
        
        return __data
    
# ===================== combined ===================== #
    
class Combined(pygame.sprite.Sprite):
    """
    Class to combine different sprites.
    """

    def __init__(self, __spriteList):
        super().__init__()
        # Combine the rects of the separate sprites.
        self.rect = __spriteList[0].rect.copy()
        for __sprite in __spriteList[1:]:
            self.rect.union_ip(__sprite.rect)

        # Create a new transparent image with the combined size.
        self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA)

        # Now blit all sprites onto the new surface.
        for __sprite in __spriteList:
            self.image.blit(__sprite.image, (__sprite.rect.x-self.rect.left,
                                           __sprite.rect.y-self.rect.top))