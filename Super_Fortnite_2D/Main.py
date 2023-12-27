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
        
        self.__tileMap = TileMap()
        self.__player = Player()
        
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
        self.__player.horizontalMovement(self.__input)
        self.__player.jump(self.__input)
    
    def drawOnScreen(self):
        self.__canvas.fill((0, 180, 240))
        self.__player.draw(self.__canvas)
        self.__tileMap.draw(self.__canvas)
        self.__window.blit(self.__canvas, (0, 0))
        pygame.display.flip()