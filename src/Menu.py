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
        self._keyinput = KeyInput()
        self._screensizeinfo = pygame.display.Info()
        self._screenresolution = pygame.math.Vector2(self._screensizeinfo.current_w, self._screensizeinfo.current_h)
        self._screen = pygame.display.set_mode((self._screenresolution.x, self._screenresolution.y))
        self._clock = pygame.time.Clock()
        self._mousepos = pygame.mouse.get_pos()
        self._currentlevel = None
        self._currentlevelbackground = None

    def drawButton(self, buttonimagepath, buttonoffsetX, buttonoffsetY):
        """
        Function that uses a path and offset of the button to create the position and image on the screen.
        Returns the rect value of the button coordinates.
        """

        # uses the given path to load the image
        button = pygame.image.load(buttonimagepath) 

        # creates an area _buttonrect with the coordinates we want the button to be in
        self._buttonrect = button.get_rect()
        self._leftborder = self._screenresolution.x // 2 - self._buttonrect.width // 2 - buttonoffsetY
        self._topborder = self._screenresolution.y // 2 - self._buttonrect.height // 2 - buttonoffsetX
        self._buttonrect = pygame.Rect(
            self._leftborder,
            self._topborder,
            self._buttonrect.width,
            self._buttonrect.height)

        # draws the image of the button onto the screen
        self._screen.blit(button, (self._leftborder, self._topborder))

        # returns the coordinates of the rect to test for interactions
        return self._buttonrect
    
    def drawBackground(self, backgroundimagepath):
        """
        Method to blit a background image onto the screen with a given path.
        """

        # uses the given path to draw the background
        _background = pygame.image.load(backgroundimagepath)
        _background = pygame.transform.scale(_background,(self._screenresolution))
        self._screen.blit(_background, (0, 0))

# ===================== main menu ===================== #

    def drawMainMenu(self):
        """
        Method to fully initate the creation of the main menu.
        """

        pygame.display.set_caption("super main menu")

        # loads in the objects and draws the main menu
        self.drawBackground("sprites/placeholder/mainmenu.png")
        self._buttonplay_rect = self.drawButton("sprites/placeholder/buttonplay.png", 150, 0)
        self._buttonquit_rect = self.drawButton("sprites/placeholder/buttonquit.png", -150, 0)
        pygame.display.flip()

    def mainMenuLoop(self):
        """
        Loop used for the main menu. Returns "levelmenu" or "quit" on specific input, otherwise returns "mainmenu".
        """

        # frame and input update
        self.drawMainMenu()
        self._keyinput.getInput()
        self._mousepos = pygame.mouse.get_pos()

        # input check
        if self._keyinput.keymouseleft:

            if self._buttonplay_rect.collidepoint(self._mousepos):
                self._keyinput.keymouseleft = False
                return "levelmenu"
        
            if self._buttonquit_rect.collidepoint(self._mousepos):
                return "quit"
            
        if self._keyinput.keyescape: # thats the RAGEQUIT button :D
            return "quit"

        # no input --> reinitialises own loop
        self._clock.tick(30)
        return "mainmenu"

# ===================== level menu ===================== #

    def drawLevelMenu(self):
        """
        Method to fully initate the creation of the level menu.
        """

        pygame.display.set_caption("super level menu")

        # loads in the objects and draws the level menu
        self.drawBackground("sprites/placeholder/levelmenu.png")
        self._level_1_rect = self.drawButton("sprites/placeholder/level1.png", 250, 500)
        pygame.display.flip()

    def levelMenuLoop(self):
        """
        Loop used for the level menu. Returns "gameloop" or "mainmenu" on specific input, otherwise returns "levelmenu".
        """

        # frame and input update
        self.drawLevelMenu()
        self._keyinput.getInput()
        self._mousepos = pygame.mouse.get_pos()

        # input check
        if self._keyinput.keyescape:
            self._keyinput.keyescape = False
            return "mainmenu"

        if self._keyinput.keymouseleft and self._level_1_rect.collidepoint(self._mousepos):
            self._currentlevel = "sprites/placeholder/level1.csv"
            self._currentlevelbackground = "sprites/placeholder/level1background.png"
            self._keyinput.keymouseleft = False
            return "gameloop"
        
        # no input --> reinitialises own loop
        self._clock.tick(30)
        return "levelmenu"
        
# ===================== game menu ===================== #

    def gameLoop(self):
        """
        Loop used for the game. Returns "pausemenu" on specific input, otherwise runs indefinetly.
        """

        # loop initiation
        self._mainloop = Game(self._screenresolution, self._currentlevel, self._currentlevelbackground)
        running = True

        while running:
            # input update
            self._keyinput.getInput()
            self._mainloop.run(self._keyinput, self._screen)

            # condition to end the running process
            if self._keyinput.keyescape:
                self._keyinput.keyescape = False
                running = False
            
            self._clock.tick(60)
        
        # after the loop is done, return to main menu
        return "mainmenu" #TODO replace mainmenu with pausemenu in this instance
    
# ===================== pause menu ===================== #
                
    def drawPauseMenu(self):
        pass
    # TODO sets the background to a blurred or darker current game frame
    # TODO button to resume, quit to main menu and to quit the game
