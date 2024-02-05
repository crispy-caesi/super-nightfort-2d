# ===================== import ===================== #

import pygame
from Game import Game
from Input import KeyInput

# ===================== menu ===================== #

class Menu():
    """
    Class to create and display different screens for menus and the gameloop.
    """

    def __init__(self):
        pygame.display.init()
        self.__keyInput = KeyInput()
        self.__screenSizeInfo = pygame.display.Info()
        self.__screenResolution = pygame.math.Vector2(self.__screenSizeInfo.current_w, self.__screenSizeInfo.current_h)
        self.__screen = pygame.display.set_mode((self.__screenResolution.x, self.__screenResolution.y))
        self.__clock = pygame.time.Clock()
        self.__mousePosition = pygame.mouse.get_pos()
        self.__currentLevel = None
        self.__currentLevelBackground = None

    def drawButton(self, __buttonImagePath, __buttonOffsetX, __buttonOffsetY):
        """
        Function that uses a path and offset of the button to create the position and image on the screen.
        Returns the rect value of the button coordinates.
        """

        # uses the given path to load the image
        button = pygame.image.load(__buttonImagePath) 

        # creates an area _buttonrect with the coordinates we want the button to be in
        self.__buttonRect = button.get_rect()
        self.__leftBorder = self.__screenResolution.x // 2 - self.__buttonRect.width // 2 - __buttonOffsetY
        self.__topBorder = self.__screenResolution.y // 2 - self.__buttonRect.height // 2 - __buttonOffsetX
        self.__buttonRect = pygame.Rect(
            self.__leftBorder,
            self.__topBorder,
            self.__buttonRect.width,
            self.__buttonRect.height)

        # draws the image of the button onto the screen
        self.__screen.blit(button, (self.__leftBorder, self.__topBorder))

        # returns the coordinates of the rect to test for interactions
        return self.__buttonRect
    
    def drawBackground(self, __backgroundImagePath):
        """
        Method to blit a background image onto the screen with a given path.
        """

        # uses the given path to draw the background
        __background = pygame.image.load(__backgroundImagePath)
        __background = pygame.transform.scale(__background,(self.__screenResolution))
        self.__screen.blit(__background, (0, 0))

# ===================== main menu ===================== #

    def drawMainMenu(self):
        """
        Method to fully initate the creation of the main menu.
        """

        pygame.display.set_caption("super main menu")

        # loads in the objects and draws the main menu
        self.drawBackground("sprites/placeholder/mainmenu.png")
        self.__buttonPlayRect = self.drawButton("sprites/placeholder/buttonplay.png", 150, 0)
        self.__buttonQuitRect = self.drawButton("sprites/placeholder/buttonquit.png", -150, 0)
        pygame.display.flip()

    def mainMenuLoop(self):
        """
        Loop used for the main menu. Returns "levelmenu" or "quit" on specific input, otherwise returns "mainmenu".
        """

        # frame and input update
        self.drawMainMenu()
        self.__keyInput.getInput()
        self.__mousePosition = pygame.mouse.get_pos()

        # input check
        if self.__keyInput.keymouseleft:

            if self.__buttonPlayRect.collidepoint(self.__mousePosition):
                self.__keyInput.keymouseleft = False
                return "levelmenu"
        
            if self.__buttonQuitRect.collidepoint(self.__mousePosition):
                return "quit"
            
        if self.__keyInput.keyescape: # thats the RAGEQUIT button :D
            return "quit"

        # no input --> reinitialises own loop
        self.__clock.tick(30)
        return "mainmenu"

# ===================== level menu ===================== #

    def drawLevelMenu(self):
        """
        Method to fully initate the creation of the level menu.
        """

        pygame.display.set_caption("super level menu")

        # loads in the objects and draws the level menu
        self.drawBackground("sprites/placeholder/levelmenu.png")
        self.__level_1_Rect = self.drawButton("sprites/placeholder/level1.png", 250, 500)
        pygame.display.flip()

    def levelMenuLoop(self):
        """
        Loop used for the level menu. Returns "gameloop" or "mainmenu" on specific input, otherwise returns "levelmenu".
        """

        # frame and input update
        self.drawLevelMenu()
        self.__keyInput.getInput()
        self.__mousePosition = pygame.mouse.get_pos()

        # input check
        if self.__keyInput.keyescape:
            self.__keyInput.keyescape = False
            return "mainmenu"

        if self.__keyInput.keymouseleft and self.__level_1_Rect.collidepoint(self.__mousePosition):
            self.__currentLevel = "sprites/placeholder/level1.csv"
            self.__currentLevelBackground = "sprites/placeholder/level1background.png"
            self.__keyInput.keymouseleft = False
            return "gameloop"
        
        # no input --> reinitialises own loop
        self.__clock.tick(30)
        return "levelmenu"
        
# ===================== game menu ===================== #

    def gameLoop(self):
        """
        Loop used for the game. Returns "pausemenu" on specific input, otherwise runs indefinetly.
        """

        # loop
        self.__mainLoop = Game(self.__screenResolution, self.__currentLevel, self.__currentLevelBackground)
        self.__mainLoop.running(self.__screen)
        return "mainmenu" #TODO replace mainmenu with pausemenu in this instance
    
# ===================== pause menu ===================== #
                
    def drawPauseMenu(self):
        pass
    # TODO sets the background to a blurred or darker current game frame
    # TODO button to resume, quit to main menu and to quit the game
