# ===================== import ===================== #

import pygame

# ===================== input ===================== #

class KeyInput():
    """
    Class to check all of the inputs a player can make in the game.
    """

    def __init__(self) -> None:
        pygame.event.set_allowed([pygame.KEYUP, pygame.KEYDOWN])
        self.__key_left:bool = False
        self.__key_right:bool = False
        self.__key_space:bool = False
        self.__key_escape:bool = False
        self.__key_hard_escape:bool = False
        self.__key_mouse_left:bool = False
        self.__key_space_pressed:bool = False #__keyspacePressed is for the sound

# ======= properties ======= #

    @property
    def key_left(self) -> bool:
        return self.__key_left

    @property
    def key_right(self) -> bool:
        return self.__key_right

    @property
    def key_space(self) -> bool:
        return self.__key_space

    @property
    def key_space_pressed(self) -> bool:
        return self.__key_space_pressed
    
    @key_space_pressed.setter
    def key_space_pressed(self, reset:bool):
        self.__key_space_pressed = reset
    
    @property
    def key_escape(self) -> bool:
        return self.__key_escape

    @key_escape.setter
    def key_escape(self, reset:bool):
        self.__key_escape = reset

    @property
    def key_mouse_left(self) -> bool:
        return self.__key_mouse_left
    
    @key_mouse_left.setter
    def key_mouse_left(self, reset:bool):
        self.__key_mouse_left = reset

    @property
    def key_hard_escape(self) -> bool:
        return self.__key_hard_escape

# ======= check for inputs ======= #

    def getInput(self) -> None:
        """
        Method to handle input events.
        """
        for event in pygame.event.get():

            # activates on button press
            if event.type == pygame.KEYDOWN:

                # list of occurable button presses
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.__key_left = True

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.__key_right = True

                elif event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    self.__key_space = True
                    self.__key_space_pressed = True      

                elif event.key == pygame.K_ESCAPE:
                    self.__key_escape = True

            # activates on button releases
            if event.type == pygame.KEYUP:

                # list of occurable button releases
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.__key_left = False

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.__key_right = False

                elif event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    self.__key_space = False

                elif event.key == pygame.K_ESCAPE:
                    self.__key_escape = False

            # special event handler for mouse input // activates on press
            if event.type == pygame.MOUSEBUTTONDOWN:

                # list of activatable mouse button presses
                if event.button == 1:
                    self.__key_mouse_left = True

            # special event handler for mouse input // activates on release
            if event.type == pygame.MOUSEBUTTONUP:

                # list of activatable mouse button releases
                if event.button == 1:
                    self.__key_mouse_left = False

            if event.type == pygame.QUIT:
                self.__key_hard_escape = True
