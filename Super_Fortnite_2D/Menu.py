# ===================== import ===================== #

import pygame
from Main import Main
import Input

# ===================== menu class parent ===================== #

class Menu():

    def __init__(self):
        pygame.display.init()
        self._keyinput = Input.KeyInput()
        self._screensize = pygame.display.Info()
        self._width, self._height = self._screensize.current_w, self._screensize.current_h
        self._screen = pygame.display.set_mode((self._width, self._height))
        self._clock = pygame.time.Clock()
        self._mousepos = pygame.mouse.get_pos()
    def drawbutton(self, buttonimagepath, buttonoffset_x, buttonoffset_y):
        # uses the given path to load the image
        button = pygame.image.load(buttonimagepath) 

        # creates an area _buttonrect with the coordinates we want the button to be in
        self._buttonrect = button.get_rect()
        self._leftborder = self._width // 2 - self._buttonrect.width // 2 - buttonoffset_y
        self._topborder = self._height // 2 - self._buttonrect.height // 2 - buttonoffset_x
        self._buttonrect = pygame.Rect(
            self._leftborder,
            self._topborder,
            self._width // 2 + self._buttonrect.width // 2 - buttonoffset_y,   # right border
            self._height // 2 + self._buttonrect.height // 2 - buttonoffset_x  # bottom border
            )
        # draws the image of the button onto the screen
        pygame.draw.rect(self._screen, 0, self._buttonrect)
        self._screen.blit(button, (self._leftborder, self._topborder))

        # returns the coordinates of the rect to test for interactions
        return self._buttonrect
    
    def drawbackground(self, backgroundimagepath):
        # uses the given path to draw the background
        _background = pygame.image.load(backgroundimagepath)
        self._screen.blit(_background, (0, 0))

# ===================== main menu ===================== #

    def drawmainmenu(self):
        pygame.display.set_caption("super main menu")

        # loads in the objects and draws it
        self.drawbackground("sprites/placeholder/mainmenu.png")
        self._buttonplay_rect = self.drawbutton("sprites/placeholder/buttonplay.png", 150, 0)
        self._buttonquit_rect = self.drawbutton("sprites/placeholder/buttonquit.png", -150, 0)
        pygame.display.flip()

    def mainmenuloop(self):
        self.drawmainmenu()
        self._keyinput.getinput()
        self._mousepos = pygame.mouse.get_pos()
        print(f"{self._buttonplay_rect}, {self._mousepos}")
        if self._keyinput.keymouseleft:

            if self._buttonplay_rect.collidepoint(self._mousepos): # thats the play button   
                self._keyinput.keymouseleft = False
                return "levelmenu"
        
            if self._buttonquit_rect.collidepoint(self._mousepos): # thats the quit button
                return "quit"
            
        if self._keyinput.keyescape:
            self._keyinput.keyescape = False
            return "quit"

        self._clock.tick(30)
        return "mainmenu"

# ===================== level menu ===================== #

    def drawlevelmenu(self):
        pygame.display.set_caption("super level menu")

        # loads in the objects and draws it
        self.drawbackground("sprites/placeholder/levelmenu.png")
        self._level_1_rect = self.drawbutton("sprites/placeholder/level1.png", 250, 500)
        pygame.display.flip()

    def levelmenuloop(self):
        self.drawlevelmenu()
        self._keyinput.getinput()
        self._mousepos = pygame.mouse.get_pos()
        if self._keyinput.keyescape:
            self._keyinput.keyescape = False
            return "mainmenu"
            
        if self._keyinput.keymouseleft and self._level_1_rect.collidepoint(self._mousepos): # thats the first level
            self._keyinput.keymouseleft = False
            return "gameloop"
        
        self._clock.tick(30)
        return "levelmenu"
        
# ===================== game menu ===================== #

class GameLoop(Menu):
    
    def __init__(self):
        super().__init__()
        self._mainloop = Main()

    def gameloop(self):
        while True:
            self._mainloop.run()
            #self._keyinput.getinput()
            if Input.KeyInput.keyescape:
                Input.KeyInput.keymouseleft = False
                return "mainmenu" #TODO replace mainmenu with pausemenu in this instance
            if not Input.KeyInput.running:
                pygame.quit
            self._clock.tick(30)

# ===================== pause menu ===================== #
                
class PauseMenu(Menu):

    def __init__(self):
        super().__init__()
        pygame.display.set_caption("super pause menu")
    # TODO sets the background to a blurred or darker current game frame
    # TODO button to resume, quit to main menu and to quit the game
