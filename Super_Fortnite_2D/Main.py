import pygame
from Input import Input_
from TileMap import TileMap
from Player import Player

class Main():
    def __init__(self):
        pygame.init()
        self.__running:bool = True
        
        self.__input = Input_()
        self.__input.setRunning(self.__running)
              
        # Display
        self.__DISPLAY_W, self.__DISPLAY_H = 900, 200
        
        self.__canvas = pygame.Surface((self.__DISPLAY_W,self.__DISPLAY_H))
        
        self.__window = pygame.display.set_mode((self.__DISPLAY_W,self.__DISPLAY_H))
        pygame.display.set_caption('Super Fortnite 2D')
        
        # clock
        self.__clock = pygame.time.Clock()
        
        #sprites
        self.__tileMap = TileMap()
        self.__player = Player()
        
        self.__all_sprites = pygame.sprite.Group()
        self.__all_sprites.add(self.__tileMap)
        self.__all_sprites.add(self.__player)
        
        #run-method - the main loop
        self.run()
    
    def run(self):
        """
        main loop
        """
        while self.__running:
            self.__input.getinput()
            self.__running = self.__input.getRunning()
            
            self.update()
            self.drawOnScreen()
            
            
    def update(self):
        
        #TODO Beendigung der Collisionen, hier nur ein Anfang --> damit man die Graviation hinzufügen kann
        if pygame.sprite.collide_mask(self.__player, self.__tileMap):
            print("Collision")
        else:
            self.__player.horizontalMovement(self.__input)
            self.__player.jump(self.__input)
        
        
    
    def drawOnScreen(self):
        self.__all_sprites.update()
        
        # camera - calculate the offset
        player_offset_x = self.__DISPLAY_W // 6 - self.__player.rect.centerx # // 6 -> more of the left site
        player_offset_y = self.__DISPLAY_H // 2 - self.__player.rect.centery # // 2 -> center
        
        
        self.__canvas.fill((0, 180, 240))
        
        # camera - move all sprites in the other direction
        for sprite in self.__all_sprites:
            sprite.rect.x += player_offset_x
            sprite.rect.y += player_offset_y
            
        self.__all_sprites.draw(self.__canvas)
        self.__window.blit(self.__canvas, (0, 0))
        pygame.display.flip()
        self.__clock.tick(30)