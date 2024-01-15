# ===================== import ===================== #

import pygame
from Main import Main
import Input

# ===================== menu class parent ===================== #

class Menu():

    def __init__(self):
        self._screensize = pygame.display.Info()
        self._width, self._height = self._screensize.current_w, self._screensize.current_h
        self._screen = pygame.display.set_mode((self._width, self._height))
        self._mousepos = pygame.mouse.get_pos()

    def drawbutton(self, buttonimagepath, buttonoffset_x, buttonoffset_y):
        # uses the given path to load the image
        button = pygame.image.load(buttonimagepath) 

        # creates an area _buttonrect with the coordinates we want the button to be in
        buttonheight, buttonwidth = button.get_rect(), button.get_rect()
        leftborder = self._width // 2 - buttonwidth // 2 - buttonoffset_y
        topborder = self._height // 2 - buttonheight // 2 - buttonoffset_x
        self._buttonrect = pygame.Rect(
            leftborder,
            topborder,
            self._width // 2 + buttonwidth // 2 - buttonoffset_y,   # right border
            self._height // 2 + buttonheight // 2 - buttonoffset_x  # bottom border
            )
        # draws the image of the button onto the screen
        self._screen.blit(button, (leftborder, topborder))

        # returns the coordinates of the rect to test for interactions
        return self._buttonrect
    
    def drawbackground(self, backgroundimagepath):
        # uses the given path to draw the background
        _background = pygame.image.load(backgroundimagepath)
        self._screen.blit(_background, (0, 0))

    def draw():
        pygame.display.flip()
    
# ===================== main menu ===================== #

class MainMenu(Menu):

    def __init__(self):
        super.__init__()
        pygame.display.set_caption("super main menu")

        # loads in the background and draws it
        self.drawbackground("sprites/placeholder/mainmenu.png")

        # initiates the creation of buttons
        self._button_1_rect = self.drawbutton("sprites/placeholder/button1.png", 100, 0)
        self._button_2_rect = self.drawbutton("sprites/placeholder/button2.png", -100, 0)

        # run
        self.mainmenuloop()

    def mainmenuloop(self):
        while True:
            self.draw()
            if Input.KeyInput.keymouse and self._button_1_rect.collidepoint(self._mousepos): # thats the play button   
                return "LEVELMENU"
            if Input.KeyInput.keymouse and self._button_2_rect.collidepoint(self._mousepos): # thats the quit button
                pygame.quit()

# ===================== level menu ===================== #

class LevelMenu(Menu):

    def __init__(self):
        super.__init__()
        pygame.display.set_caption("super level menu")

        # loads in the background and draws it
        self.drawbackground("sprites/placeholder/levelmenu.png")

        # initiates the creation of the level buttons
        self._level_1_rect = self.drawbutton("sprite/placeholder/level1.png",self._width//3, self._height//2)

        # run
        self.levelmenuloop()

    def levelmenuloop(self):
        while True:
            self.draw()
            if Input.KeyInput.keyescape:
                return "MAINMENU"
            if Input.KeyInput.keymouse and self._level_1_rect.collidepoint(self._mousepos): # thats the first level
                return "GAMELOOP"

# ===================== game menu ===================== #

class GameLoop(Menu):
    
    def __init__(self):
        super.__init__()
        self._mainloop = Main()

        # run
        self.gameloop()

    def gameloop(self):
        while True:
            self._mainloop.run()
            if Input.KeyInput.keyescape:
                return "MAINMENU" #TODO replace mainmenu with pausemenu in this instance
            if not Input.KeyInput.running:
                pygame.quit
            #Input.KeyInput.getinput() test, if not working, enable this

# ===================== pause menu ===================== #
                
class PauseMenu(Menu):

    def __init__(self):
        super.__init__()
        pygame.display.set_caption("super pause menu")
    # TODO sets the background to a blurred or darker current game frame
    # TODO button to resume, quit to main menu and to quit the game

"""
TODO:
alter main.py to draw on the menu.py surface
"""