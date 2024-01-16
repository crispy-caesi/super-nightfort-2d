# ===================== import ===================== #

import pygame
from TileMap import TileMap
from Player import Player

# ===================== Main ===================== #

class Game():
    """
    Class that fuses all of the subparts together for the game to be playable.
    """

    def __init__(self, screenwidth, screenheight, currentlevel):
        pygame.init()
        self._screenwidth, self._screenheight = screenwidth, screenheight
        self._tileMap = TileMap(currentlevel)
        self._player = Player()
        self._all_sprites = pygame.sprite.Group()
        self._all_sprites.add(self._tileMap)
        self._all_sprites.add(self._player)
        self._background = pygame.image.load("sprites/placeholder/level1background.png")

    def drawgameframe(self):
        """
        Method to blit the game on the screen.
        """
        
        self._all_sprites.update()
        
        # camera - calculate the offset
        player_offset_x = self._screenwidth // 6 - self._player.rect.centerx    # more on the left site
        player_offset_y = self._screenheight // 2 - self._player.rect.centery   # center
        
        # camera - move all sprites in the other direction
        for sprite in self._all_sprites:
            sprite.rect.x += player_offset_x
            sprite.rect.y += player_offset_y

        # draws the current frame on the screen
        self._screen.blit(self._background, (0, 0))
        self._all_sprites.draw(self._screen)
        #TODO UI health
        #TODO UI score
        pygame.display.flip()

# ======= game loop ======= #

    def run(self, input, screen):
        """
        Method that lets the game update and run in one.
        """

        # runs all of Game.py main functions
        self._screen = screen
        self._input = input
        self._player.playerupdate(keyinput = self._input, tilemaprect = self._tileMap)
        self._tileMap.updatePosition()
        self.drawgameframe()
