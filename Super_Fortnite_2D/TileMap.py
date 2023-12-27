import pygame
import csv

class Tile(pygame.sprite.Sprite):
    """
    Class to create a single tile
    """

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


class TileMap(pygame.sprite.Sprite):
    def __init__(self, csvPath:str = "sprites/placeholder/big_level.csv"):
        super().__init__()
        tiles = []     
            
        lst = self.readCSV( filePath = csvPath)
        
        for column in range(len(lst)):
            for row in range(len(lst[0])):
                if lst[column][row] == "4":
                   tile = Tile("sprites/placeholder/Duck.png", row * 16, column * 16)
                   tiles.append(tile)
                if  lst[column][row] == "1":
                   tile = Tile("sprites/placeholder/Grass.png", row * 16, column * 16)
                   tiles.append(tile)
                if lst[column][row] == "2":
                   tile = Tile("sprites/placeholder/Dirt.png", row * 16, column * 16) 
                   tiles.append(tile)
                   
        combined = Combined(tiles)
        self.image = combined.image
        self.rect = self.image.get_rect()
                    
                
        
    
    def draw(self, surface):
        surface.blit(self.image, (0,0))
    
    def readCSV(self, filePath:str)->list:
        data = [[]]
        try:
            file = open(filePath, "r")  
            data = list(csv.reader(file, delimiter=","))
            file.close()
        except:
            print("Can't read csv file")
        
        return data
    

class Combined(pygame.sprite.Sprite):

    def __init__(self, sprites):
        super().__init__()
        # Combine the rects of the separate sprites.
        self.rect = sprites[0].rect.copy()
        for sprite in sprites[1:]:
            self.rect.union_ip(sprite.rect)

        # Create a new transparent image with the combined size.
        self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        # Now blit all sprites onto the new surface.
        for sprite in sprites:
            self.image.blit(sprite.image, (sprite.rect.x-self.rect.left,
                                           sprite.rect.y-self.rect.top))
            
    
if __name__ == "__main__":
    map = TileMap()