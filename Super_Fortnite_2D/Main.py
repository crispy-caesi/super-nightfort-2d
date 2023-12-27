import pygame
from Input import Input

class Main():
    def __init__(self):
        self.__running:bool = True
        
        self.__input = Input()
        self.__input.setRunning(self.__running)
              
        # Display
        self.__DISPLAY_W, self.__DISPLAY_H = 200, 200
        
        self.__canvas = pygame.Surface((self.__DISPLAY_W,self.__DISPLAY_H))
        
        self.__window = pygame.display.set_mode((self.__DISPLAY_W,self.__DISPLAY_H))
        
        #run-method - the main loop
        self.run()
    
    def run(self):
        """
        main loop
        """
        while self.__running:
            self.__input.getinput()
            self.__running = self.__input.getRunning()
            
    
    def events(self):
        pass
    
    def update(self):
        pass
