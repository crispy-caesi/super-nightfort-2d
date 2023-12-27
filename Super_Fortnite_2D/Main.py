import pygame
from Input import Input
from TileMap import TileMap

class Main():
    def __init__(self):
        pygame.init()
        self.__running:bool = True
        
        self.__input = Input()
        self.__input.setRunning(self.__running)
              
        # Display
        self.__DISPLAY_W, self.__DISPLAY_H = 200, 200
        
        self.__canvas = pygame.Surface((self.__DISPLAY_W,self.__DISPLAY_H))
        
        self.__window = pygame.display.set_mode((self.__DISPLAY_W,self.__DISPLAY_H))
        
        
        self.__tileMap = TileMap()
        
        #run-method - the main loop
        self.run()
    
    def run(self):
        """
        main loop
        """
        while self.__running:
            self.__input.getinput()
            self.__running = self.__input.getRunning()
            
            self.drawOnScreen()
            
    
    def events(self):
        pass
    
    def update(self):
        pass
    
    def drawOnScreen(self):
        self.__canvas.fill((0, 180, 240))
        self.__tileMap.draw(self.__canvas)
        self.window.blit(self.canvas, (0, 0))