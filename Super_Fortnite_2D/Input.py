# ===================== import ===================== #

import pygame

# ===================== input ===================== #

class KeyInput():

    """
    Class to check all of the inputs a player can make in the game.
    """

    def __init__(self):
        # game is running
        self.__running:bool = True

        # player buttons preset
        self.__keyleft:bool = False
        self.__keyright:bool = False
        self.__keyspace:bool = False
    
    @property
    def running(self):
        return self.__running
    
    @property
    def getkeyleft(self):
        return self.__keyleft

    @property
    def getkeyright(self):
        return self.__keyright

    @property
    def getkeyspace(self):
        return self.__keyspace

    # check for inputs
    def getinput(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                KeyInput.running(False)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    self.__keyleft = True

                elif event.key == pygame.K_RIGHT:
                    self.__keyright = True

                elif event.key == pygame.K_SPACE:
                    self.__keyspace = True

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                    self.__keyleft = False

                elif event.key == pygame.K_RIGHT:
                    self.__keyright = False

                elif event.key == pygame.K_SPACE:
                    self.__keyspace = False