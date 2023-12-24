# ===================== import ===================== #

import pygame, csv, os

# ===================== Tile ===================== #

class Tile(pygame.sprite.Sprite):

    '''
    Class to create a single tile
    '''

    def __init__(self, image, x, y, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        # Manual load in: self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

# ===================== TileMap ===================== #

class TileMap():

    '''
    class to create the tilemap
    '''

    def __init__(self, filename, spritesheet, offset:tuple):
        self.offset = offset
        self.tile_size = 16
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def draw_map(self, surface):
        surface.blit(self.map_surface,(0,0))

    def load_map(self):

        '''
        rendering the tilemap        
        '''

        for tile in self.tiles:
            tile.draw(self.map_surface)

    def read_csv(self, filename):

        # the csv file is the one used to store the data of the level

        '''
        converts the csv file to an 2D array
        '''

        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))

        return map

    def load_tiles(self, filename):

        '''
        uses the read_csv function and connects each tile to the correct texture and size
        '''

        tiles = []
        map = self.read_csv(filename)
        x, y = 0, 0

        for row in map:
            x = 0

            for tile in row:

                # checks the type of tile and matches the texture

                if tile == '0':
                    self.start_x, self.start_y = x * self.tile_size - self.offset[0], y * self.tile_size -  self.offset[1]
                elif tile == '1':
                    tiles.append(Tile('grass.png', x * self.tile_size - self.offset[0], y * self.tile_size - self.offset[1], self.spritesheet))
                elif tile == '2':
                    tiles.append(Tile('grass2.png', x * self.tile_size - self.offset[0], y * self.tile_size - self.offset[1], self.spritesheet))
                    
                x += 1 # counter for the rows

            y += 1 # size of the tile map

        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size

        return tiles
