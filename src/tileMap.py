# ===================== import ===================== #

import pygame
import csv

# ===================== tile ===================== #

class Tile(pygame.sprite.Sprite):
    """
    Class to create a single tile.
    """

    def __init__(self, imagePath :str, x :int, y :int):
        pygame.sprite.Sprite.__init__(self)
        pre_image = pygame.image.load(imagePath).convert_alpha()
        self.__image = pygame.transform.scale(pre_image, (pre_image.get_width() // 2, pre_image.get_height() // 2))
        self.__rect = self.__image.get_rect()
        self.__rect.x, self.__rect.y = x, y

    @property
    def image(self)->pygame.surface.Surface:
        return self.__image
    
    @property
    def rect(self)->pygame.rect.Rect:
        return self.__rect

# ===================== tilemap ===================== #
        
class TileMap(pygame.sprite.Sprite):
    """
    Class to create the tilemap with which other objects can interact.
    """
    
    def __init__(self, csvPath:str, tile_paths:list):
        super().__init__()
        self.__tiles = []    
        self.__hurtMap = [] 
        lst = self.readCSV( filePath = csvPath)
        
        for column in range(len(lst)):
            for row in range(len(lst[0])):
                if lst[column][row] == "0": # dirt
                   tile = Tile(tile_paths[0], row * 16, column * 16 )
                   self.__tiles.append(tile)
                if lst[column][row] == "1": # dirt
                   tile = Tile(tile_paths[1], row * 16, column * 16 )
                   self.__tiles.append(tile)
                if lst[column][row] == "2": # dirt
                   tile = Tile(tile_paths[2], row * 16, column * 16 )
                   self.__tiles.append(tile)
                if lst[column][row] == "3": # dirt
                   tile = Tile(tile_paths[3], row * 16, column * 16 )
                   self.__tiles.append(tile)
                if lst[column][row] == "4": # spikes16
                   tile = Tile(tile_paths[4], row * 16, column * 16 )
                   self.__hurtMap.append(tile.rect)
                   self.__tiles.append(tile)
                if lst[column][row] == "5": # dirt
                   tile = Tile(tile_paths[5], row * 16, column * 16 )
                   self.__tiles.append(tile)
                if lst[column][row] == "6": # dirt
                   tile = Tile(tile_paths[6], row * 16, column * 16 )
                   self.__tiles.append(tile)
                if lst[column][row] == "7": # dirt
                   tile = Tile(tile_paths[7], row * 16, column * 16 )
                   self.__tiles.append(tile)
                if lst[column][row] == "8": # dirt
                   tile = Tile(tile_paths[8], row * 16, column * 16 )
                   self.__tiles.append(tile)
                if lst[column][row] == "9": # dirt
                   tile = Tile(tile_paths[9], row * 16, column * 16 )
                   self.__tiles.append(tile)
                if lst[column][row] == "10": # dirt
                   tile = Tile(tile_paths[10], row * 16, column * 16 )
                   self.__tiles.append(tile)

        combined = Combined(self.__tiles)
        self.__image = combined.image
        self.__rect = self.__image.get_rect()

    @property
    def image(self)->pygame.surface.Surface:
        return self.__image
    
    @property
    def rect(self)->pygame.rect.Rect:
        return self.__rect

    @property
    def hurtMap(self):
        return self.__hurtMap

    def updateTilemapPosition(self):
        self.prev_x = self.__rect.x
        self.prev_y = self.__rect.y

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

    def __init__(self, spriteList :list):
        super().__init__()
        # Combine the rects of the separate sprites.
        rect = spriteList[0].rect.copy()
        for sprite in spriteList[1:]:
            rect.union_ip(sprite.rect)

        # Create a new transparent image with the combined size.
        self.__image = pygame.Surface(rect.size, pygame.SRCALPHA)

        # Now blit all sprites onto the new surface.
        for sprite in spriteList:
            self.__image.blit(sprite.image, (sprite.rect.x-rect.left,
                                           sprite.rect.y-rect.top))

    @property
    def image(self)->pygame.surface.Surface:
        return self.__image
