# ===================== import ===================== #

import pygame

# ===================== input ===================== #

class Input():

    '''
    Class to check all of the inputs a player can make in the game.
    '''

    def __init__(self):

        # game is running
        self.isRunning = True
        
        # player presses buttons
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.SPACE_KEY = False

    def getinput(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    self.isRunning = False

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