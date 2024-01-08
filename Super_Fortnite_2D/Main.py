import pygame
from Input import KeyInput
from TileMap import TileMap
from Player import Player

class Main():
    def __init__(self):
        pygame.init()
        self._running:bool = True
        
        self._input = KeyInput()
        self._input.running = self._running
              
        # Display
        self._DISPLAY_W, self._DISPLAY_H = 900, 200
        
        self._canvas = pygame.Surface((self._DISPLAY_W,self._DISPLAY_H))
        
        self._window = pygame.display.set_mode((self._DISPLAY_W,self._DISPLAY_H))
        pygame.display.set_caption('Super Fortnite 2D')
        
        # clock
        self._clock = pygame.time.Clock()
        
        #sprites
        self._tileMap = TileMap()
        self._player = Player()
        
        self._all_sprites = pygame.sprite.Group()
        self._all_sprites.add(self._tileMap)
        self._all_sprites.add(self._player)
        
        #run-method - the main loop
        self.run()
    
    def run(self):
        """
        main loop
        """
        while self._running:
            self._input.getinput()
            self._running = self._input.running
            
            self.update()
            self.drawOnScreen()
            
            
    def update(self):

        self._player.playerupdate(keyinput = self._input, tilemaprect = self._tileMap)
        self._tileMap.updatePosition()
    
        ### debug ###
        #print(f"Collision: {pygame.sprite.collide_mask(self._player, self._tileMap)}")
        #print(f"Position Tilemap: {self._tileMap.rect.x}")
        #print(f"Position Player: {self._player.rect.x}")

    def drawOnScreen(self):
        self._all_sprites.update()
        
        # camera - calculate the offset
        player_offset_x = self._DISPLAY_W // 6 - self._player.rect.centerx # // 6 -> more of the left site
        player_offset_y = self._DISPLAY_H // 2 - self._player.rect.centery # // 2 -> center
        
        
        self._canvas.fill((0, 180, 240))
        
        # camera - move all sprites in the other direction
        for sprite in self._all_sprites:
            sprite.rect.x += player_offset_x
            sprite.rect.y += player_offset_y
            
        self._all_sprites.draw(self._canvas)
        self._window.blit(self._canvas, (0, 0))
        pygame.display.flip()
        self._clock.tick(30)