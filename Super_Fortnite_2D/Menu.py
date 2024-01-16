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
        self._screensize = pygame.display.Info()
        self._screenwidth, self._screenheight = self._screensize.current_w, self._screensize.current_h
        self._screen = pygame.display.set_mode((self._screenwidth, self._screenheight))
        self._clock = pygame.time.Clock()
        self._mousepos = pygame.mouse.get_pos()
        self._currentlevel = None

    def drawbutton(self, buttonimagepath, buttonoffset_x, buttonoffset_y):
        """
        Function that uses a path and offset of the button to create the position and image on the screen.
        Returns the rect value of the button coordinates.
        """

        # uses the given path to load the image
        button = pygame.image.load(buttonimagepath) 

        # creates an area _buttonrect with the coordinates we want the button to be in
        self._buttonrect = button.get_rect()
        self._leftborder = self._screenwidth // 2 - self._buttonrect.width // 2 - buttonoffset_y
        self._topborder = self._screenheight // 2 - self._buttonrect.height // 2 - buttonoffset_x
        self._buttonrect = pygame.Rect(
            self._leftborder,
            self._topborder,
            self._buttonrect.width,
            self._buttonrect.height)

        # draws the image of the button onto the screen
        self._screen.blit(button, (self._leftborder, self._topborder))

        # returns the coordinates of the rect to test for interactions
        return self._buttonrect
    
    def drawbackground(self, backgroundimagepath):
        """
        Method to blit a background image onto the screen with a given path.
        """

        # uses the given path to draw the background
        _background = pygame.image.load(backgroundimagepath)
        self._screen.blit(_background, (0, 0))

# ===================== main menu ===================== #

    def drawmainmenu(self):
        """
        Method to fully initate the creation of the main menu.
        """

        pygame.display.set_caption("super main menu")

        # loads in the objects and draws the main menu
        self.drawbackground("sprites/placeholder/mainmenu.png")
        self._buttonplay_rect = self.drawbutton("sprites/placeholder/buttonplay.png", 150, 0)
        self._buttonquit_rect = self.drawbutton("sprites/placeholder/buttonquit.png", -150, 0)
        pygame.display.flip()

    def mainmenuloop(self):
        """
        Loop used for the main menu. Returns "levelmenu" or "quit" on specific input, otherwise returns "mainmenu".
        """

        # frame and input update
        self.drawmainmenu()
        self._keyinput.getinput()
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

    def drawlevelmenu(self):
        """
        Method to fully initate the creation of the level menu.
        """

        pygame.display.set_caption("super level menu")

        # loads in the objects and draws the level menu
        self.drawbackground("sprites/placeholder/levelmenu.png")
        self._level_1_rect = self.drawbutton("sprites/placeholder/level1.png", 250, 500)
        pygame.display.flip()

    def levelmenuloop(self):
        """
        Loop used for the level menu. Returns "gameloop" or "mainmenu" on specific input, otherwise returns "levelmenu".
        """

        # frame and input update
        self.drawlevelmenu()
        self._keyinput.getinput()
        self._mousepos = pygame.mouse.get_pos()

        # input check
        if self._keyinput.keyescape:
            self._keyinput.keyescape = False
            return "mainmenu"

        if self._keyinput.keymouseleft and self._level_1_rect.collidepoint(self._mousepos):
            self._currentlevel = "sprites/placeholder/level1.csv"
            self._keyinput.keymouseleft = False
            return "gameloop"
        
        # no input --> reinitialises own loop
        self._clock.tick(30)
        return "levelmenu"
        
# ===================== game menu ===================== #

    def gameloop(self):
        """
        Loop used for the game. Returns "pausemenu" on specific input, otherwise runs indefinetly.
        """

        # loop initiation
        self._mainloop = Game(self._screenwidth, self._screenheight, self._currentlevel)
        running = True

        while running:
            # input update
            self._keyinput.getinput()
            self._mainloop.run(self._keyinput, self._screen)

            # condition to end the running process
            if self._keyinput.keyescape:
                self._keyinput.keyescape = False
                running = False
            
            self._clock.tick(120)
        
        # after the loop is done, return to main menu
        return "mainmenu" #TODO replace mainmenu with pausemenu in this instance
    
# ===================== pause menu ===================== #
                
    def drawpausemenu(self):
        pass
    # TODO sets the background to a blurred or darker current game frame
    # TODO button to resume, quit to main menu and to quit the game
