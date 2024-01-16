# ===================== import ===================== #

import pygame

# ===================== input ===================== #

class KeyInput():
    """
    Class to check all of the inputs a player can make in the game.
    """

    def __init__(self):
        self._keyleft = False
        self._keyright = False
        self._keyspace = False
        self._keyescape = False
        self._keymouseleft = False

# ======= properties ======= #

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
    def keyescape(self, reset:bool):
        self._keyescape = reset

    @property
    def keymouseleft(self):
        return self._keymouseleft
    
    @keymouseleft.setter
    def keymouseleft(self, reset:bool):
        self._keymouseleft = reset

# ======= check for inputs ======= #

    def getInput(self):
        """
        Method to handle input events.
        """
        
        for event in pygame.event.get():
            
            # activates on button press
            if event.type == pygame.KEYDOWN:
                
                # list of occurable button presses
                if event.key == pygame.K_LEFT:
                    self._keyleft = True

                elif event.key == pygame.K_RIGHT:
                    self._keyright = True

                elif event.key == pygame.K_SPACE:
                    self._keyspace = True

                elif event.key == pygame.K_ESCAPE:
                    self._keyescape = True

            # activates on button releases
            if event.type == pygame.KEYUP:

                # list of occurable button releases
                if event.key == pygame.K_LEFT:
                    self._keyleft = False

                elif event.key == pygame.K_RIGHT:
                    self._keyright = False

                elif event.key == pygame.K_SPACE:
                    self._keyspace = False
                
                elif event.key == pygame.K_ESCAPE:
                    self._keyescape = False

            # special event handler for mouse input // activates on press
            if event.type == pygame.MOUSEBUTTONDOWN:

                # list of activatable mouse button presses
                if event.button == 1:
                    self._keymouseleft = True
                """
                elif event.button == 2:
                    middle mouse button
                    
                elif event.button == 3:
                    right mouse button
                    
                elif event.button == 4:
                    mouse wheel up
                    
                elif event.button == 5:
                    mouse wheel down
                """
            # special event handler for mouse input // activates on release
            if event.type == pygame.MOUSEBUTTONUP:

                # list of activatable mouse button releases
                if event.button == 1:
                    self._keymouseleft = False
                """
                elif event.button == 2:
                    middle mouse button
                elif event.button == 3:
                    right mouse button
                elif event.button == 4:
                    mouse wheel up
                elif event.button == 5:
                    mouse wheel down
                """