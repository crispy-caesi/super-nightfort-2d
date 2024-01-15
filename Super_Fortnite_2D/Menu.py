# ===================== import ===================== #

import pygame
import Main
import Input

# ===================== parent menu ===================== #

class Menu():

    def __init__(self):
        self._screensize = pygame.display.Info()
        self._width, self._height = self._screensize.current_w, self._screensize.current_h
        self._screen = pygame.display.set_mode((self._width, self._height))
        self._mousepos = pygame.mouse.get_pos()

    def drawbutton(self, buttonimage, buttonoffset_x, buttonoffset_y):
        # loads the image in usable form
        button = pygame.image.load(buttonimage) 

        # creates an object _buttonrect with the area we want
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
    
    def draw():
        pygame.display.flip()
    
# ===================== main menu ===================== #

class MainMenu(Menu):

    def __init__(self):
        super.__init__()
        pygame.display.set_caption("super main menu")

        # loads in the background and draws it
        self._background = pygame.image.load("sprites/placeholder/mainmenu.png")
        self._screen.blit(self._background, (0, 0))

        # initiates the creation of buttons
        self._button_1_rect = self.drawbutton("sprites/placeholder/button1.png", 100, 0)
        self._button_2_rect = self.drawbutton("sprites/placeholder/button2.png", -100, 0)

    def mainmenuloop(self):
        while True:
            self.draw()
            if Input.KeyInput.keymouse and self._button_1_rect.collidepoint(self._mousepos): # thats the play button   
                return #TODO return to "metaloop"
            if Input.KeyInput.keymouse and self._button_2_rect.collidepoint(self._mousepos): # thats the quit button
                pygame.quit()

# ===================== level menu ===================== #
                
class LevelMenu(Menu):

    def __init__(self):
        super.__init__()
        pygame.display.set_caption("super level menu")

        # loads in the background and draws it
        self._background = pygame.image.load("sprites/placeholder/levelmenu.png")
        self._screen.blit(self._background, (0, 0))

        # initiates the creation of the level buttons
        self._level_1_rect = self.drawbutton("sprite/placeholder/level1.png",self._width//3, self._height//2)

    def levelmenuloop(self, window):
        while True:
            self.draw()
            if Input.KeyInput.keyescape:
                return #TODO return to "metaloop"
            if self._level_1_rect.collidepoint(self._mousepos):
                return #TODO return to "metaloop"

# ===================== game menu ===================== #
            
class GameLoop(Menu):
    
    def __init__(self):
        super.__init__()
        self._mainloop = Main()
        #TODO run the main game here