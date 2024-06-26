# ===================== import ===================== #

import pygame

# ===================== input ===================== #

class KeyInput():
    """
    Class to check all of the inputs a player can make in the game.
    """

    def __init__(self):
        pygame.event.set_allowed([pygame.KEYUP, pygame.KEYDOWN])
        self.__keyleft = False
        self.__keyright = False
        self.__keyspace = False
        self.__keyescape = False
        self.__keymouseleft = False
        self.__keyspacePressed = False #__keyspacePressed is for the sound

# ======= properties ======= #

    @property
    def keyleft(self):
        return self.__keyleft

    @property
    def keyright(self):
        return self.__keyright

    @property
    def keyspace(self):
        return self.__keyspace

    @property
    def keyspacePressed(self):
        return self.__keyspacePressed
    
    @keyspacePressed.setter
    def keyspacePressed(self, reset:bool):
        self.__keyspacePressed = reset
    
    @property
    def keyescape(self):
        return self.__keyescape

    @keyescape.setter
    def keyescape(self, reset:bool):
        self.__keyescape = reset

    @property
    def keymouseleft(self):
        return self.__keymouseleft
    
    @keymouseleft.setter
    def keymouseleft(self, reset:bool):
        self.__keymouseleft = reset

# ======= check for inputs ======= #

    def getInput(self):
        """
        Method to handle input events.
        """
        
        for event in pygame.event.get():
            
            # activates on button press
            if event.type == pygame.KEYDOWN:
                
                # list of occurable button presses
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.__keyleft = True

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.__keyright = True

                elif event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    self.__keyspace = True
                    self.__keyspacePressed = True      

                elif event.key == pygame.K_ESCAPE:
                    self.__keyescape = True

            # activates on button releases
            if event.type == pygame.KEYUP:

                # list of occurable button releases
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.__keyleft = False

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.__keyright = False

                elif event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    self.__keyspace = False
                
                elif event.key == pygame.K_ESCAPE:
                    self.__keyescape = False

            # special event handler for mouse input // activates on press
            if event.type == pygame.MOUSEBUTTONDOWN:

                # list of activatable mouse button presses
                if event.button == 1:
                    self.__keymouseleft = True
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
                    self.__keymouseleft = False
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