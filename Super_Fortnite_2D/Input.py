# ===================== import ===================== #

import pygame

# ===================== input ===================== #

class KeyInput():

    '''
    Class to check all of the inputs a player can make in the game.
    '''

    def __init__(self):

        # game is running
        self.running:bool = True
        
        # player presses buttons
        self.LEFT_KEY:bool = False
        self.RIGHT_KEY:bool = False
        self.SPACE_KEY:bool = False
        
    def getRunning(self):
        return self.running
    
    def setRunning(self, running):
        self.running = running

    def getkeyleft(self):
        return self.LEFT_KEY

    def getkeyright(self):
        return self.RIGHT_KEY

    def getkeyspace(self):
        return self.SPACE_KEY
    def getinput(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    self.running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True

                elif event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True

                elif event.key == pygame.K_SPACE:
                    self.SPACE_KEY = True

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = False

                elif event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = False

                elif event.key == pygame.K_SPACE:
                    self.SPACE_KEY = False