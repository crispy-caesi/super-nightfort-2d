# ===================== import ===================== #

import pygame
from PIL import Image
from Game import Game
from Input import KeyInput
import os

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
        self.__currentCharacterSkin = None

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

    def mergeImage(self, __imageTopPath, __imageBottomPath, __newImageName):
        """
        Method to merge two images to create a single image
        """
        
        __imageTop = Image.open(__imageTopPath)
        __imageBottom = Image.open(__imageBottomPath)
        __imageBottom.paste(__imageTop, (0,0))#, mask = __imageTop)
        __imageBottom.save(__newImageName) 

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
        self.__level_1_Rect = self.drawButton("sprites/icons/level_icons/level1.png", 250, 500)
        self.__level_2_Rect = self.drawButton("sprites/icons/level_icons/level2.png", 250, 250)
        self.__level_3_Rect = self.drawButton("sprites/icons/level_icons/level3.png", 250, 0)
        self.__level_4_Rect = self.drawButton("sprites/icons/level_icons/level4.png", 250, -250)
        self.__level_5_Rect = self.drawButton("sprites/icons/level_icons/level5.png", 250, -500)

        pygame.display.flip()

    def levelMenuLoop(self):
        """
        Loop used for the level menu. Returns "levelmenu" or "mainmenu" on specific input, otherwise returns "levelmenu".
        """

        # frame and input update
        self.drawLevelMenu()
        self.__keyInput.getInput()
        self.__mousePosition = pygame.mouse.get_pos()
        self.__tiles_path = []

        # input check
        if self.__keyInput.keyescape:
            self.__keyInput.keyescape = False
            return "mainmenu"

        if self.__keyInput.keymouseleft and self.__level_1_Rect.collidepoint(self.__mousePosition):
            self.__currentLevel = "sprites/blocks/csv/level1_grassland.csv"
            self.__currentLevelBackground = "sprites/placeholder/level1background.png"
            self.__keyInput.keymouseleft = False
            self.__tiles_path = self.get_file_names("sprites/blocks/grassland")
            print(self.get_file_names("sprites/blocks/grassland"))
            return "charactermenu"
        
        if self.__keyInput.keymouseleft and self.__level_2_Rect.collidepoint(self.__mousePosition):
            self.__currentLevel = "sprites/blocks/csv/level2_desert.csv"
            self.__currentLevelBackground = "sprites/placeholder/level1background.png"
            self.__keyInput.keymouseleft = False
            self.__tiles_path = self.get_file_names("sprites/blocks/desert")
            print(self.__tiles_path)
            return "charactermenu"
        
        if self.__keyInput.keymouseleft and self.__level_3_Rect.collidepoint(self.__mousePosition):
            self.__currentLevel = "sprites/blocks/csv/level3_grassland.csv"
            self.__currentLevelBackground = "sprites/placeholder/level1background.png"
            self.__keyInput.keymouseleft = False
            self.__tiles_path = self.get_file_names("sprites/blocks/grassland_2")
            print(self.__tiles_path)
            return "charactermenu"
        
        if self.__keyInput.keymouseleft and self.__level_4_Rect.collidepoint(self.__mousePosition):
            self.__currentLevel = "sprites/blocks/csv/level4_snowland.csv"
            self.__currentLevelBackground = "sprites/placeholder/level1background.png"
            self.__keyInput.keymouseleft = False
            self.__tiles_path = self.get_file_names("sprites/blocks/snowland")
            print(self.__tiles_path)
            return "charactermenu"
        
        if self.__keyInput.keymouseleft and self.__level_5_Rect.collidepoint(self.__mousePosition):
            self.__currentLevel = "sprites/blocks/csv/level5_test.csv"
            self.__currentLevelBackground = "sprites/placeholder/level1background.png"
            self.__keyInput.keymouseleft = False
            self.__tiles_path = self.get_file_names("sprites/blocks/grassland")
            print(self.__tiles_path)
            return "charactermenu"
        
        # no input --> reinitialises own loop
        self.__clock.tick(30)
        return "levelmenu"
    

    def get_file_names(self, directory):
        file_names = []
        files = os.listdir(directory)
        # Sortiere die Dateinamen alphabetisch
        files.sort(key=lambda x: int(x.split('sprite_')[1].split('.')[0]))
        for filename in files:
            if os.path.isfile(os.path.join(directory, filename)):
                file_names.append(os.path.join(directory, filename))
        return file_names


    
# ===================== character menu ===================== #
    
    def drawCharacterMenu(self):
        """
        Method to fully initate the creation of the character menu.
        """

        pygame.display.set_caption("super character menu")

        # loads in the objects and draws the level menu
        self.drawBackground("sprites/placeholder/mainmenu.png") # replace with new sprite

        # button for the Fich
        self.mergeImage("sprites/characters/fich/fich.gif","sprites/icons/character_background.gif","sprites/characters/fich/buttonImage.gif")
        self.__buttonFichRect = self.drawButton("sprites/characters/fich/buttonImage.gif", 250, 500)

        # button for the Meister Wu
        self.mergeImage("sprites/characters/wu/wu.gif","sprites/icons/character_background.gif","sprites/characters/wu/buttonImage.gif")
        self.__buttonWuRect = self.drawButton("sprites/characters/wu/buttonImage.gif", 250, 250)

        # button for the Amogus
        self.mergeImage("sprites/characters/amogus/amogus_image.gif","sprites/icons/character_background.gif","sprites/characters/amogus/buttonImage.gif")
        self.__buttonAmogusRect = self.drawButton("sprites/characters/amogus/buttonImage.gif", 250, 0)

        # button for the Pacman
        self.mergeImage("sprites/characters/pacman/pacman_image.gif","sprites/icons/character_background.gif","sprites/characters/pacman/buttonImage.gif")
        self.__buttonPacmanRect = self.drawButton("sprites/characters/pacman/buttonImage.gif", 250, -250)

        # button for the Po
        self.mergeImage("sprites/characters/poo/po.gif","sprites/icons/character_background.gif","sprites/characters/poo/buttonImage.gif")
        self.__buttonPoRect = self.drawButton("sprites/characters/poo/buttonImage.gif", 250, -500)
        pygame.display.flip()

    def characterMenuLoop(self):
        """
        Loop used for the character menu. Returns "gameloop" or "levelmenu" on specific input, otherwise returns "charactermenu".
        """

        # frame and input update
        self.drawCharacterMenu()
        self.__keyInput.getInput()
        self.__mousePosition = pygame.mouse.get_pos()

        # input check
        if self.__keyInput.keyescape:
            self.__keyInput.keyescape = False
            return "levelmenu"
        
        if self.__keyInput.keymouseleft and self.__buttonWuRect.collidepoint(self.__mousePosition):
            self.__currentCharacterSkin = "sprites/characters/wu/wu_image.gif"
            self.__death_path =  "sprites/characters/wu/wu_death.gif"
            self.__jump_path = "sprites/characters/wu/wu_jump.gif"
            self.__keyInput.keymouseleft = False
            return "gameloop"
        
        if self.__keyInput.keymouseleft and self.__buttonFichRect.collidepoint(self.__mousePosition):
            self.__currentCharacterSkin = "sprites/characters/fich/fich_image.gif"
            self.__death_path =  "sprites/characters/fich/fich_death.gif"
            self.__jump_path = "sprites/characters/fich/fich_jump.gif"
            self.__keyInput.keymouseleft = False
            return "gameloop"
        
        if self.__keyInput.keymouseleft and self.__buttonAmogusRect.collidepoint(self.__mousePosition):
            self.__currentCharacterSkin = "sprites/characters/amogus/amogus_image.gif"
            self.__death_path =  "sprites/characters/amogus/amogus_death.gif"
            self.__jump_path = "sprites/characters/amogus/amogus_jump.gif"
            self.__keyInput.keymouseleft = False
            return "gameloop"
        
        if self.__keyInput.keymouseleft and self.__buttonPacmanRect.collidepoint(self.__mousePosition):
            self.__currentCharacterSkin = "sprites/characters/pacman/pacman_image.gif"
            self.__death_path =  "sprites/characters/pacman/pacman_death.gif"
            self.__jump_path = "sprites/characters/pacman/pacman_jump.gif"
            self.__keyInput.keymouseleft = False
            return "gameloop"
        
        if self.__keyInput.keymouseleft and self.__buttonPoRect.collidepoint(self.__mousePosition):
            self.__currentCharacterSkin = "sprites/characters/poo/po_image.gif"
            self.__death_path =  "sprites/characters/poo/po_death.gif"
            self.__jump_path = "sprites/characters/poo/po_jump.gif"
            self.__keyInput.keymouseleft = False
            return "gameloop"
        
        # no input --> reinitialises own loop
        self.__clock.tick(30)
        return "charactermenu"
        
# ===================== game menu ===================== #

    def gameLoop(self):
        """
        Loop used for the game. Returns "pausemenu" on specific input, otherwise runs indefinetly.
        """

        # loop
        self.__mainLoop = Game(
            self.__screenResolution,
            self.__currentLevel,
            self.__currentLevelBackground,
            self.__currentCharacterSkin,
            self.__death_path,
            self.__jump_path,
            self.__tiles_path)
        
        self.__mainLoop.running(self.__screen)
        return "mainmenu" #TODO replace mainmenu with pausemenu in this instance
    
# ===================== pause menu ===================== #
                
    def drawPauseMenu(self):
        pass
    # TODO sets the background to a blurred or darker current game frame
    # TODO button to resume, quit to main menu and to quit the game