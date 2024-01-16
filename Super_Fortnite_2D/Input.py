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
        self._keymouseleft:bool = False
        
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

    @keyescape.setter
    def keyescape(self, reset):
        self._keyescape = reset

    @property
    def keymouseleft(self):
        return self._keymouseleft
    
    @keymouseleft.setter
    def keymouseleft(self, reset):
        self._keymouseleft = reset
        
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

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                    self._keyleft = False

                elif event.key == pygame.K_RIGHT:
                    self._keyright = False

                elif event.key == pygame.K_SPACE:
                    self._keyspace = False
                
                elif event.key == pygame.K_ESCAPE:
                    self._keyescape = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    self._keymouseleft = True

                #elif event.button == 2:
                #    print("middle mouse button")
                #elif event.button == 3:
                #    print("right mouse button")
                #elif event.button == 4:
                #    print("mouse wheel up")
                #elif event.button == 5:
                #    print("mouse wheel down")

            if event.type == pygame.MOUSEBUTTONUP:

                if event.button == 1:
                    self._keymouseleft = False

                #elif event.button == 2:
                #    print("middle mouse button")
                #elif event.button == 3:
                #    print("right mouse button")
                #elif event.button == 4:
                #    print("mouse wheel up")
                #elif event.button == 5:
                #    print("mouse wheel down")

