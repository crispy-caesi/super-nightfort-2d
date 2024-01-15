# ===================== import ===================== #

import pygame

# ===================== input ===================== #

class KeyInput():

    '''
    Class to check all of the inputs a player can make in the game.
    '''

    def __init__(self):
        # game is running
        self._running:bool = True
        
        # player presses buttons
        self._keyleft:bool = False
        self._keyright:bool = False
        self._keyspace:bool = False
        self._keyescape:bool = False
        self._keymouse:bool = False
        
    @property
    def running(self):
        return self._running
    
    @running.setter
    def running(self, running):
        self._running = running

    @property
    def keyleft(self):
        return self._keyleft

    @property
    def keyright(self):
        return self._keyright

    @property
    def keyspace(self):
        return self._keyspace
    
    @property
    def keyescape(self):
        return self._keyescape

    @property
    def keymouse(self):
        return self._keymouse
    
    def getinput(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    self._running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    self._keyleft = True

                elif event.key == pygame.K_RIGHT:
                    self._keyright = True

                elif event.key == pygame.K_SPACE:
                    self._keyspace = True

                elif event.key == pygame.K_ESCAPE:
                    self._keyescape = True

                elif event.key == pygame.MOUSEBUTTONDOWN:
                    self._keymouse = True

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                    self._keyleft = False

                elif event.key == pygame.K_RIGHT:
                    self._keyright = False

                elif event.key == pygame.K_SPACE:
                    self._keyspace = False
                
                elif event.key == pygame.K_ESCAPE:
                    self._keyescape = False

                elif event.key == pygame.MOUSEBUTTONUP:
                    self._keymouse = False