# ======================= imports ======================= #

import pygame
from PIL import Image
from game import Game
from inputs import KeyInput
import os

# ======================= menu template ======================= #

class Menu():
    """
    Class to create and display different screens for menus and the gameloop.
    """

    def __init__(self):
        pygame.display.init()
        self.__screenSizeInfo = pygame.display.Info()
        self.__screenResolution = pygame.math.Vector2(self.__screenSizeInfo.current_w, self.__screenSizeInfo.current_h)
        self.__screen = pygame.display.set_mode((self.__screenResolution.x, self.__screenResolution.y))

        self.__clock = pygame.time.Clock()
        self.__clock_tick = 30

    def drawButton(self, buttonImagePath :str, buttonOffsetX :int, buttonOffsetY :int):
        """
        Function that uses a path and offset of the button to create the position and image on the screen.
        Returns the rect value of the button coordinates.
        """

        # uses the given path to load the image
        button = pygame.image.load(buttonImagePath) 

        # creates an area _buttonrect with the coordinates we want the button to be in
        buttonRect = button.get_rect()
        leftBorder = self.__screenResolution.x // 2 - buttonRect.width // 2 - buttonOffsetY
        topBorder = self.__screenResolution.y // 2 - buttonRect.height // 2 - buttonOffsetX
        buttonRect = pygame.Rect(
            leftBorder,
            topBorder,
            buttonRect.width,
            buttonRect.height)

        # draws the image of the button onto the screen
        self.__screen.blit(button, (leftBorder, topBorder))

        # returns the coordinates of the rect to test for interactions
        return buttonRect
    
    def drawBackground(self, backgroundImagePath:str):
        """
        Method to blit a background image onto the screen with a given path.
        """

        # uses the given path to draw the background
        background = pygame.image.load(backgroundImagePath)
        background = pygame.transform.scale(background,(self.__screenResolution))
        self.__screen.blit(background, (0, 0))

    def mergeImage(self, imageTopPath :str, imageBottomPath :str, newImageName :str):
        """
        Method to merge two images to create a single image
        """
        
        imageTop = Image.open(imageTopPath)
        imageBottom = Image.open(imageBottomPath)
        imageBottom.paste(imageTop, (0,0))#, mask = __imageTop)
        imageBottom.save(newImageName) 
    
    def get_file_names(self, directory :str):
        file_names = []
        files = os.listdir(directory)
        # Sortiere die Dateinamen alphabetisch
        files.sort(key=lambda x: int(x.split('sprite_')[1].split('.')[0]))
        for filename in files:
            if os.path.isfile(os.path.join(directory, filename)):
                file_names.append(os.path.join(directory, filename))
        return file_names

    def getScreenResoltution(self):
        return self.__screenResolution
    

    def getScreen(self):
        return self.__screen
    
    @property
    def clockTick(self):
        return self.__clock_tick
    
# ======================= main menu ======================= #

class MainMenu(Menu):
    """
    Draws and handles interactions of main menu
    """
    def __init__(self, clock:pygame.time.Clock):
        super().__init__()
        self.__keyInput = KeyInput()
        self.__clock = clock

    
    def draw(self) -> None:
        """
        Draws all the buttons and loads the background image
        """
        pygame.display.set_caption("super main menu")
        # loads in the objects and draws the main menu
        self.drawBackground("sprites/placeholder/mainmenu.png")
        self.__buttonPlayRect = self.drawButton("sprites/placeholder/buttonplay.png", 150, 0)
        self.__buttonQuitRect = self.drawButton("sprites/placeholder/buttonquit.png", -150, 0)

        pygame.display.flip()


    def loop(self)-> str:
        """
        Loop used for the main menu. Returns "levelmenu" or "quit" on specific input, otherwise returns "mainmenu".
        """

        self.__keyInput.getInput()
        mousePosition = pygame.mouse.get_pos()

        # input check
        if self.__keyInput.keymouseleft:

            if self.__buttonPlayRect.collidepoint(mousePosition):
                self.__keyInput.keymouseleft = False
                return "levelmenu"
        
            if self.__buttonQuitRect.collidepoint(mousePosition):
                return "quit"
            
        if self.__keyInput.keyescape: # thats the RAGEQUIT button :D
            return "quit"

        # no input --> reinitialises own loop
        self.__clock.tick(self.clockTick)
        return "mainmenu"

# ======================= level menu ======================= #

class LevelMenu(Menu):
    """
    Draws and handles interactions of level menu
    """
    def __init__(self,clock:pygame.time.Clock):
        super().__init__()
        self.__keyInput = KeyInput()
        self.__clock = clock


    
    def draw(self)-> None:
        """
        Draws all the buttons and loads the background image
        """
        pygame.display.set_caption("super level menu")
        # loads in the objects and draws the level menu
        self.drawBackground("sprites/placeholder/levelmenu.png")
        self.__level_1_Rect = self.drawButton("sprites/icons/level_icons/level1.png", 250, 500)
        self.__level_2_Rect = self.drawButton("sprites/icons/level_icons/level2.png", 250, 250)
        self.__level_3_Rect = self.drawButton("sprites/icons/level_icons/level3.png", 250, 0)
        self.__level_4_Rect = self.drawButton("sprites/icons/level_icons/level4.png", 250, -250)
        self.__level_5_Rect = self.drawButton("sprites/icons/level_icons/level5.png", 250, -500)

        self.__tiles_path = []

        pygame.display.flip()

    def loop(self)->str:
        """
        Loop used for the level menu. Returns "levelmenu" or "mainmenu" on specific input, otherwise returns "levelmenu".
        """
        # frame and input update
        self.__keyInput.getInput()
        mousePosition = pygame.mouse.get_pos()
        

        # input check
        if self.__keyInput.keyescape:
            self.__keyInput.keyescape = False
            return "mainmenu"

        elif self.__keyInput.keymouseleft and self.__level_1_Rect.collidepoint(mousePosition):
            self.__currentLevel = "sprites/blocks/csv/level1_grassland.csv"
            self.__currentLevelBackground = "sprites/placeholder/level1background.png"
            self.__keyInput.keymouseleft = False
            self.__tiles_path = self.get_file_names("sprites/blocks/grassland")
            print(self.get_file_names("sprites/blocks/grassland"))
            return "charactermenu"
        
        elif self.__keyInput.keymouseleft and self.__level_2_Rect.collidepoint(mousePosition):
            self.__currentLevel = "sprites/blocks/csv/level2_desert.csv"
            self.__currentLevelBackground = "sprites/placeholder/level1background.png"
            self.__keyInput.keymouseleft = False
            self.__tiles_path = self.get_file_names("sprites/blocks/desert")
            print(self.__tiles_path)
            return "charactermenu"
        
        elif self.__keyInput.keymouseleft and self.__level_3_Rect.collidepoint(mousePosition):
            self.__currentLevel = "sprites/blocks/csv/level3_grassland.csv"
            self.__currentLevelBackground = "sprites/placeholder/level1background.png"
            self.__keyInput.keymouseleft = False
            self.__tiles_path = self.get_file_names("sprites/blocks/grassland_2")
            print(self.__tiles_path)
            return "charactermenu"
        
        elif self.__keyInput.keymouseleft and self.__level_4_Rect.collidepoint(mousePosition):
            self.__currentLevel = "sprites/blocks/csv/level4_snowland.csv"
            self.__currentLevelBackground = "sprites/placeholder/level1background.png"
            self.__keyInput.keymouseleft = False
            self.__tiles_path = self.get_file_names("sprites/blocks/snowland")
            print(self.__tiles_path)
            return "charactermenu"
        
        elif self.__keyInput.keymouseleft and self.__level_5_Rect.collidepoint(mousePosition):
            self.__currentLevel = "sprites/blocks/csv/level5_test.csv"
            self.__currentLevelBackground = "sprites/placeholder/level1background.png"
            self.__keyInput.keymouseleft = False
            self.__tiles_path = self.get_file_names("sprites/blocks/grassland")
            print(self.__tiles_path)
            return "charactermenu"
        
        # no input --> reinitialises own loop
        self.__clock.tick(self.clockTick)
        return "levelmenu"
    
    def getTilesPath(self)->list:
        return self.__tiles_path
    
    def getCurrentLevel(self)->str:
        return self.__currentLevel
    
    def getCurrentLevelBackground(self)->str:
        return self.__currentLevelBackground

# ======================= character menu ======================= #

class CharacterMenu(Menu):
    """
    Draws and handles interactions of character menu
    """
    def __init__(self, clock:pygame.time.Clock):
        """
        Method to fully initate the creation of the character menu.
        """
        super().__init__()
        self.__keyInput = KeyInput()
        self.__clock = clock


    def draw(self)-> None:
        """
        Draws all the buttons and loads the background image
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
        
    def loop(self)->str:
            """
            Loop used for the character menu. Returns "gameloop" or "levelmenu" on specific input, otherwise returns "charactermenu".
            """

            # frame and input 

            self.__keyInput.getInput()
            mousePosition = pygame.mouse.get_pos()

            # input check
            if self.__keyInput.keyescape:
                self.__keyInput.keyescape = False
                return "levelmenu"
            
            if self.__keyInput.keymouseleft and self.__buttonWuRect.collidepoint(mousePosition):
                self.__currentCharacterSkin = "sprites/characters/wu/wu_image.gif"
                self.__death_path =  "sprites/characters/wu/wu_death.gif"
                self.__jump_path = "sprites/characters/wu/wu_jump.gif"
                self.__keyInput.keymouseleft = False
                return "gameloop"
            
            if self.__keyInput.keymouseleft and self.__buttonFichRect.collidepoint(mousePosition):
                self.__currentCharacterSkin = "sprites/characters/fich/fich_image.gif"
                self.__death_path =  "sprites/characters/fich/fich_death.gif"
                self.__jump_path = "sprites/characters/fich/fich_jump.gif"
                self.__keyInput.keymouseleft = False
                return "gameloop"
            
            if self.__keyInput.keymouseleft and self.__buttonAmogusRect.collidepoint(mousePosition):
                self.__currentCharacterSkin = "sprites/characters/amogus/amogus_image.gif"
                self.__death_path =  "sprites/characters/amogus/amogus_death.gif"
                self.__jump_path = "sprites/characters/amogus/amogus_jump.gif"
                self.__keyInput.keymouseleft = False
                return "gameloop"
            
            if self.__keyInput.keymouseleft and self.__buttonPacmanRect.collidepoint(mousePosition):
                self.__currentCharacterSkin = "sprites/characters/pacman/pacman_image.gif"
                self.__death_path =  "sprites/characters/pacman/pacman_death.gif"
                self.__jump_path = "sprites/characters/pacman/pacman_jump.gif"
                self.__keyInput.keymouseleft = False
                return "gameloop"
            
            if self.__keyInput.keymouseleft and self.__buttonPoRect.collidepoint(mousePosition):
                self.__currentCharacterSkin = "sprites/characters/poo/po_image.gif"
                self.__death_path =  "sprites/characters/poo/po_death.gif"
                self.__jump_path = "sprites/characters/poo/po_jump.gif"
                self.__keyInput.keymouseleft = False
                return "gameloop"
            
            # no input --> reinitialises own loop
            self.__clock.tick(self.clockTick)
            return "charactermenu"

    def getCurrentCharacterSkin(self)->str:
        return self.__currentCharacterSkin
    
    def getJumpPath(self)->str:
        return self.__jump_path

    def getDeathPath(self)->str:
        return self.__death_path

# ======================= win menu ======================= #

class WinMenu(Menu):
    """
    Draws and handles interactions of main menu
    """
    def __init__(self):
        """
        draws the win menu or show it on the screen
        """
        super().__init__()
        self.__keyInput = KeyInput()
    
    def draw(self)-> None:
        """
        Draws buttons and background image of WinMenu
        """
        pygame.display.set_caption("you won supa nite fort")

        # loads in the objects and draws the level menu
        self.drawBackground("sprites/placeholder/level1background.png")

        self.__menuButton = self.drawButton("sprites/placeholder/menu.png", 0, 0)
        self.drawButton("sprites/placeholder/YouWin.png", 250, 0)

    def loop(self)->str:
        """
        Loop used for the menu if you win the game
        """
        self.__keyInput.getInput()
        mousePosition = pygame.mouse.get_pos()

        if self.__keyInput.keymouseleft and self.__menuButton.collidepoint(mousePosition):
            self.__keyInput.keymouseleft = False
            return "mainmenu"
        
        pygame.display.flip()
        
        return "winmenu" 
    
# ======================= game loop ======================= #

class GameLoop():
    """
    Class giving all attributes to the game, and handling the game loop
    """
    def __init__(self, screenResolution:pygame.math.Vector2, currentLevel:str, currentLevelBackground:str, currentCharacterSkin:str, death_path:str, jump_path:str, tiles_path:list, screen:pygame.surface.Surface) -> None:
        self.__screenResolution = screenResolution
        self.__currentLevel = currentLevel
        self.__currentLevelBackground = currentLevelBackground
        self.__currentCharacterSkin = currentCharacterSkin
        self.__death_path = death_path
        self.__jump_path = jump_path
        self.__tiles_path = tiles_path
        self.__screen = screen

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
        
        if self.__mainLoop.getWin():
            return "winmenu"

        return "mainmenu"
