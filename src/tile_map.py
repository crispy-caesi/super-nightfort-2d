"""module that handles generating and displaying the tilemap"""
# ===================== import ===================== #

import csv
import pygame

# ===================== tile ===================== #

class Tile(pygame.sprite.Sprite):
    """
    Class to create a single tile.
    """

    def __init__(self, image_path:str, x:int, y:int) -> int:
        pygame.sprite.Sprite.__init__(self)
        pre_image:pygame.Surface = pygame.image.load(image_path).convert_alpha()
        self.__image:pygame.Surface = pygame.transform.scale(pre_image, (pre_image.get_width() // 2, pre_image.get_height() // 2))
        self.__rect:pygame.Rect = self.__image.get_rect()
        self.__rect.x, self.__rect.y = x, y

    @property
    def image(self)->pygame.Surface:
        return self.__image

    @property
    def rect(self)->pygame.Rect:
        return self.__rect

# ===================== tilemap ===================== #

class TileMap(pygame.sprite.Sprite):
    """
    Class to create the tilemap with which other objects can interact.
    """

    def __init__(self, csv_path:str, tile_paths:list) -> None:
        super().__init__()
        self.__tiles:list[Tile] = []
        self.__hurt_map:list = []
        lst:list[list[int]] = self.read_csv( file_path = csv_path)

        self.prev_x:int
        self.prev_y:int

        for i, column in enumerate(lst):
            for j, cell in enumerate(column):
                match cell:
                    case "0": # dirt
                        tile = Tile(tile_paths[0], j * 16, i * 16 )
                        self.__tiles.append(tile)
                    case "1": # dirt
                        tile = Tile(tile_paths[1], j * 16, i * 16 )
                        self.__tiles.append(tile)
                    case "2": # dirt
                        tile = Tile(tile_paths[2], j * 16, i * 16 )
                        self.__tiles.append(tile)
                    case "3": # dirt
                        tile = Tile(tile_paths[3], j * 16, i * 16 )
                        self.__tiles.append(tile)
                    case "4": # spikes16
                        tile = Tile(tile_paths[4], j * 16, i * 16 )
                        self.__hurt_map.append(tile.rect)
                        self.__tiles.append(tile)
                    case "5": # dirt
                        tile = Tile(tile_paths[5], j * 16, i * 16 )
                        self.__tiles.append(tile)
                    case "6": # dirt
                        tile = Tile(tile_paths[6], j * 16, i * 16 )
                        self.__tiles.append(tile)
                    case "7": # dirt
                        tile = Tile(tile_paths[7], j * 16, i * 16 )
                        self.__tiles.append(tile)
                    case "8": # dirt
                        tile = Tile(tile_paths[8], j * 16, i * 16 )
                        self.__tiles.append(tile)
                    case "9": # dirt
                        tile = Tile(tile_paths[9], j * 16, i * 16 )
                        self.__tiles.append(tile)
                    case "10": # dirt
                        tile = Tile(tile_paths[10], j * 16, i * 16 )
                        self.__tiles.append(tile)

        combined = Combined(self.__tiles)
        self.__image = combined.image
        self.__rect = self.__image.get_rect()

    @property
    def image(self) -> pygame.Surface:
        return self.__image

    @property
    def rect(self) -> pygame.Rect:
        return self.__rect

    @property
    def hurt_map(self):
        return self.__hurt_map

    def update_tilemap_position(self) -> None:
        self.prev_x = self.__rect.x
        self.prev_y = self.__rect.y

    def read_csv(self, file_path:str) -> list[list[int]]:
        """
        Reads a CSV file and returns its values as a list
        """
        data:list[list[int]] = [[]]

        with open(file_path, "r", encoding="utf-8") as file:
            data = list(csv.reader(file, delimiter=","))

        return data

# ===================== combined ===================== #

class Combined(pygame.sprite.Sprite):
    """
    Class to combine different sprites.
    """

    def __init__(self, sprite_list :list) -> None:
        super().__init__()
        # Combine the rects of the separate sprites.
        rect = sprite_list[0].rect.copy()
        for sprite in sprite_list[1:]:
            rect.union_ip(sprite.rect)

        # Create a new transparent image with the combined size.
        self.__image = pygame.Surface(rect.size, pygame.SRCALPHA)

        # Now blit all sprites onto the new surface.
        for sprite in sprite_list:
            self.__image.blit(sprite.image, (sprite.rect.x-rect.left,
                                           sprite.rect.y-rect.top))

    @property
    def image(self) -> pygame.Surface:
        return self.__image
