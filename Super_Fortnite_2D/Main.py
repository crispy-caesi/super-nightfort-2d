import pygame

class Main():
    def __init__(self):
        self.__running:bool = True
        
        # Display
        self.__DISPLAY_W, self.__DISPLAY_H = 200, 200
        
        self.__canvas = pygame.Surface((self.__DISPLAY_W,self.__DISPLAY_H))
        
        self.__window = pygame.display.set_mode((self.__DISPLAY_W,self.__DISPLAY_H))
        
        #run-method - the main loop
        self.run()
    
    def run(self):
        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
    
    def events(self):
        pass
    
    def update(self):
        pass
