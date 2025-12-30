"""module which takes care of the GUI"""

# ======================= imports ======================= #

import os
import typing
import pygame
from PIL import Image
from game import Game
from inputs import KeyInput

# ======================= menu template ======================= #

class Menu():
    """
    Class to create and display different screens for menus and the gameloop.
    """

    def __init__(self) -> None:
        pygame.display.init()
        self.__screen_size_info = pygame.display.Info()
        self.__screen_resolution:pygame.Vector2 = pygame.Vector2(self.__screen_size_info.current_w, self.__screen_size_info.current_h)
        self.__screen:pygame.Surface = pygame.display.set_mode((self.__screen_resolution.x, self.__screen_resolution.y))

        self.__clock_tick:int = 30

    def draw_button(self, button_image_path :str, button_offset_x :int, button_offset_y :int) -> pygame.Rect:
        """
        Function that uses a path and offset of the button to create the position and image on the screen.
        Returns the rect value of the button coordinates.
        """

        # uses the given path to load the image
        button:pygame.Surface = pygame.image.load(button_image_path)

        # creates an area _buttonrect with the coordinates we want the button to be in
        button_rect:pygame.Rect = button.get_rect()
        left_border:int = self.__screen_resolution.x // 2 - button_rect.width // 2 - button_offset_y
        top_border:int = self.__screen_resolution.y // 2 - button_rect.height // 2 - button_offset_x
        button_rect:pygame.Rect = pygame.Rect(
            left_border,
            top_border,
            button_rect.width,
            button_rect.height)

        # draws the image of the button onto the screen
        self.__screen.blit(button, (left_border, top_border))

        # returns the coordinates of the rect to test for interactions
        return button_rect
    
    def draw_background(self, background_image_path:str) -> None:
        """
        Method to blit a background image onto the screen with a given path.
        """

        # uses the given path to draw the background
        background: pygame.Surface = pygame.image.load(background_image_path)
        background = pygame.transform.scale(background,(self.__screen_resolution))
        self.__screen.blit(background, (0, 0))
    
    def get_file_names(self, directory :str) -> list[str]:
        """
        return all names of the file in a directory 
        """
        file_names:list = []
        files:list[str] = os.listdir(directory)
        # Sortiere die Dateinamen alphabetisch
        files.sort(key=lambda x: int(x.split('sprite_')[1].split('.')[0]))
        for filename in files:
            if os.path.isfile(os.path.join(directory, filename)):
                file_names.append(os.path.join(directory, filename))
        return file_names

    def get_screen_resoltution(self) -> pygame.Vector2:
        return self.__screen_resolution
    

    def get_screen(self) -> pygame.Surface:
        return self.__screen
    
    @property
    def clock_tick(self) -> int:
        return self.__clock_tick
    
# ======================= main menu ======================= #

class MainMenu(Menu):
    """
    Draws and handles interactions of main menu
    """
    def __init__(self, clock:pygame.time.Clock):
        super().__init__()
        self.__key_input:KeyInput = KeyInput()

        self.__button_play_rect:pygame.Rect
        self.__button_quit_rect:pygame.Rect

        self.__clock:pygame.time.Clock = clock

    
    def draw(self) -> None:
        """
        Draws all the buttons and loads the background image
        """
        pygame.display.set_caption("super main menu")
        # loads in the objects and draws the main menu
        self.draw_background("sprites/backgrounds/mainmenu.png")
        self.__button_play_rect:pygame.Rect = self.draw_button("sprites/buttons/buttonplay.png", 150, 0)
        self.__button_quit_rect:pygame.Rect = self.draw_button("sprites/buttons/buttonquit.png", -150, 0)

        pygame.display.flip()


    def loop(self)-> str:
        """
        Loop used for the main menu. Returns "levelmenu" or "quit" on specific input, otherwise returns "mainmenu".
        """

        self.__key_input.getInput()
        mouse_position:typing.Tuple[int, int] = pygame.mouse.get_pos()

        # input check
        if self.__key_input.keymouseleft:

            if self.__button_play_rect.collidepoint(mouse_position):
                self.__key_input.keymouseleft = False
                return "levelmenu"

            if self.__button_quit_rect.collidepoint(mouse_position):
                return "quit"

        if self.__key_input.keyescape or self.__key_input.keyhardescape: # thats the RAGEQUIT button :D
            return "quit"


        # no input --> reinitialises own loop
        self.__clock.tick(self.clock_tick)
        return "mainmenu"

# ======================= level menu ======================= #

class LevelMenu(Menu):
    """
    Draws and handles interactions of level menu
    """
    def __init__(self,clock:pygame.time.Clock) -> None:
        super().__init__()
        self.__key_input:KeyInput = KeyInput()

        self.__current_level:str
        self.__current_level_background:str

        self.__tiles_path:list[str] = []
        self.__level_1_rect:pygame.Rect
        self.__level_2_rect:pygame.Rect
        self.__level_3_rect:pygame.Rect
        self.__level_4_rect:pygame.Rect
        self.__level_5_rect:pygame.Rect

        self.__clock = clock
    
    def draw(self)-> None:
        """
        Draws all the buttons and loads the background image
        """
        pygame.display.set_caption("super level menu")

        # loads in the objects and draws the level menu
        self.draw_background("sprites/backgrounds/levelmenu.png")

        self.__level_1_rect = self.draw_button("sprites/buttons/level_icons/level1.png", 250, 500)
        self.__level_2_rect = self.draw_button("sprites/buttons/level_icons/level2.png", 250, 250)
        self.__level_3_rect = self.draw_button("sprites/buttons/level_icons/level3.png", 250, 0)
        self.__level_4_rect = self.draw_button("sprites/buttons/level_icons/level4.png", 250, -250)
        self.__level_5_rect = self.draw_button("sprites/buttons/level_icons/level5.png", 250, -500)

        pygame.display.flip()

    def loop(self) -> str:
        """
        Loop used for the level menu. Returns "levelmenu" or "mainmenu" on specific input, otherwise returns "levelmenu".
        """
        # frame and input update
        self.__key_input.getInput()
        mouse_position:typing.Tuple[int, int] = pygame.mouse.get_pos()


        # input check
        if self.__key_input.keyescape:
            self.__key_input.keyescape = False
            return "mainmenu"

        elif self.__key_input.keymouseleft and self.__level_1_rect.collidepoint(mouse_position):
            self.__current_level = "sprites/blocks/csv/level1_grassland.csv"
            self.__current_level_background = "sprites/backgrounds/level1background.png"
            self.__key_input.keymouseleft = False
            self.__tiles_path = self.get_file_names("sprites/blocks/grassland")
            print(self.get_file_names("sprites/blocks/grassland"))
            return "charactermenu"

        elif self.__key_input.keymouseleft and self.__level_2_rect.collidepoint(mouse_position):
            self.__current_level = "sprites/blocks/csv/level2_desert.csv"
            self.__current_level_background = "sprites/backgrounds/level1background.png"
            self.__key_input.keymouseleft = False
            self.__tiles_path = self.get_file_names("sprites/blocks/desert")
            print(self.__tiles_path)
            return "charactermenu"

        elif self.__key_input.keymouseleft and self.__level_3_rect.collidepoint(mouse_position):
            self.__current_level = "sprites/blocks/csv/level3_grassland.csv"
            self.__current_level_background = "sprites/backgrounds/level1background.png"
            self.__key_input.keymouseleft = False
            self.__tiles_path = self.get_file_names("sprites/blocks/grassland_2")
            print(self.__tiles_path)
            return "charactermenu"

        elif self.__key_input.keymouseleft and self.__level_4_rect.collidepoint(mouse_position):
            self.__current_level = "sprites/blocks/csv/level4_snowland.csv"
            self.__current_level_background = "sprites/backgrounds/level1background.png"
            self.__key_input.keymouseleft = False
            self.__tiles_path = self.get_file_names("sprites/blocks/snowland")
            print(self.__tiles_path)
            return "charactermenu"

        elif self.__key_input.keymouseleft and self.__level_5_rect.collidepoint(mouse_position):
            self.__current_level = "sprites/blocks/csv/level5_test.csv"
            self.__current_level_background = "sprites/backgrounds/level1background.png"
            self.__key_input.keymouseleft = False
            self.__tiles_path = self.get_file_names("sprites/blocks/grassland")
            print(self.__tiles_path)
            return "charactermenu"

        if self.__key_input.keyhardescape:
            return "quit"

        # no input --> reinitialises own loop
        self.__clock.tick(self.clock_tick)
        return "levelmenu"

    def get_tiles_path(self) -> list:
        return self.__tiles_path

    def get_current_level(self) -> str:
        return self.__current_level

    def get_current_level_background(self) -> str:
        return self.__current_level_background

# ======================= character menu ======================= #

class CharacterMenu(Menu):
    """
    Draws and handles interactions of character menu
    """
    def __init__(self, clock:pygame.time.Clock) -> None:
        """
        Method to fully initate the creation of the character menu.
        """
        super().__init__()
        self.__key_input:KeyInput = KeyInput()
        self.__clock:pygame.time.Clock = clock

        self.__button_fich_rect:pygame.Rect
        self.__button_wu_rect:pygame.Rect
        self.__button_amogus_rect:pygame.Rect
        self.__button_pacman_rect:pygame.Rect
        self.__button_po_rect:pygame.Rect

        self.__current_character_skin:str
        self.__death_path:str
        self.__jump_path:str

    def merge_image(self, image_top_path :str, image_bottom_path :str, new_image_name :str) -> None:
        """
        Method to merge two images to create a single image
        """

        image_top:Image = Image.open(image_top_path)
        image_bottom:Image = Image.open(image_bottom_path)
        image_bottom.paste(image_top, (0,0))#, mask = __imageTop)
        image_bottom.save(new_image_name)

    def draw(self) -> None:
        """
        Draws all the buttons and loads the background image
        """
        pygame.display.set_caption("super character menu")

        # loads in the objects and draws the level menu
        self.draw_background("sprites/backgrounds/mainmenu.png") # replace with new sprite

        # button for the Fich
        self.merge_image("sprites/characters/fich/fich.gif","sprites/buttons/character_background.gif","sprites/characters/fich/buttonImage.gif")
        self.__button_fich_rect = self.draw_button("sprites/characters/fich/buttonImage.gif", 250, 500)

        # button for the Meister Wu
        self.merge_image("sprites/characters/wu/wu.gif","sprites/buttons/character_background.gif","sprites/characters/wu/buttonImage.gif")
        self.__button_wu_rect = self.draw_button("sprites/characters/wu/buttonImage.gif", 250, 250)

        # button for the Amogus
        self.merge_image("sprites/characters/amogus/amogus_image.gif","sprites/buttons/character_background.gif","sprites/characters/amogus/buttonImage.gif")
        self.__button_amogus_rect = self.draw_button("sprites/characters/amogus/buttonImage.gif", 250, 0)

        # button for the Pacman
        self.merge_image("sprites/characters/pacman/pacman_image.gif","sprites/buttons/character_background.gif","sprites/characters/pacman/buttonImage.gif")
        self.__button_pacman_rect = self.draw_button("sprites/characters/pacman/buttonImage.gif", 250, -250)

        # button for the Po
        self.merge_image("sprites/characters/poo/po.gif","sprites/buttons/character_background.gif","sprites/characters/poo/buttonImage.gif")
        self.__button_po_rect = self.draw_button("sprites/characters/poo/buttonImage.gif", 250, -500)
        pygame.display.flip()

    def loop(self) -> str:
        """
        Loop used for the character menu. Returns "gameloop" or "levelmenu" on specific input, otherwise returns "charactermenu".
        """
        # frame and input

        self.__key_input.getInput()
        mouse_position:typing.Tuple[int, int] = pygame.mouse.get_pos()

        # input check
        if self.__key_input.keyescape:
            self.__key_input.keyescape = False
            return "levelmenu"

        if self.__key_input.keyhardescape:
            return "quit"

        if self.__key_input.keymouseleft and self.__button_wu_rect.collidepoint(mouse_position):
            self.__current_character_skin = "sprites/characters/wu/wu_image.gif"
            self.__death_path =  "sprites/characters/wu/wu_death.gif"
            self.__jump_path = "sprites/characters/wu/wu_jump.gif"
            self.__key_input.keymouseleft = False
            return "gameloop"

        if self.__key_input.keymouseleft and self.__button_fich_rect.collidepoint(mouse_position):
            self.__current_character_skin = "sprites/characters/fich/fich_image.gif"
            self.__death_path =  "sprites/characters/fich/fich_death.gif"
            self.__jump_path = "sprites/characters/fich/fich_jump.gif"
            self.__key_input.keymouseleft = False
            return "gameloop"

        if self.__key_input.keymouseleft and self.__button_amogus_rect.collidepoint(mouse_position):
            self.__current_character_skin = "sprites/characters/amogus/amogus_image.gif"
            self.__death_path =  "sprites/characters/amogus/amogus_death.gif"
            self.__jump_path = "sprites/characters/amogus/amogus_jump.gif"
            self.__key_input.keymouseleft = False
            return "gameloop"

        if self.__key_input.keymouseleft and self.__button_pacman_rect.collidepoint(mouse_position):
            self.__current_character_skin = "sprites/characters/pacman/pacman_image.gif"
            self.__death_path =  "sprites/characters/pacman/pacman_death.gif"
            self.__jump_path = "sprites/characters/pacman/pacman_jump.gif"
            self.__key_input.keymouseleft = False
            return "gameloop"

        if self.__key_input.keymouseleft and self.__button_po_rect.collidepoint(mouse_position):
            self.__current_character_skin = "sprites/characters/poo/po_image.gif"
            self.__death_path = "sprites/characters/poo/po_death.gif"
            self.__jump_path = "sprites/characters/poo/po_jump.gif"
            self.__key_input.keymouseleft = False
            return "gameloop"

        # no input --> reinitialises own loop
        self.__clock.tick(self.clock_tick)
        return "charactermenu"

    def get_current_character_skin(self)->str:
        return self.__current_character_skin

    def get_jump_path(self)->str:
        return self.__jump_path

    def get_death_path(self)->str:
        return self.__death_path

# ======================= win menu ======================= #

class WinMenu(Menu):
    """
    Draws and handles interactions of main menu
    """
    def __init__(self) -> None:
        """
        draws the win menu or show it on the screen
        """
        super().__init__()
        self.__key_input:KeyInput = KeyInput()
        self.__menu_button:pygame.Rect
    
    def draw(self) -> None:
        """
        Draws buttons and background image of WinMenu
        """
        pygame.display.set_caption("you won supa nite fort")

        # loads in the objects and draws the level menu
        self.draw_background("sprites/backgrounds/level1background.png")

        self.__menu_button = self.draw_button("sprites/buttons/menu.png", 0, 0)
        self.draw_button("sprites/buttons/YouWin.png", 250, 0)

    def loop(self) -> str:
        """
        Loop used for the menu if you win the game
        """
        self.__key_input.getInput()
        mouse_position:typing.Tuple[int, int] = pygame.mouse.get_pos()

        if self.__key_input.keymouseleft and self.__menu_button.collidepoint(mouse_position):
            self.__key_input.keymouseleft = False
            return "mainmenu"

        if self.__key_input.keyhardescape:
            return "quit"

        pygame.display.flip()

        return "winmenu"

# ======================= game loop ======================= #
class GameLoop():
    """
    Class giving all attributes to the game, and handling the game loop
    """
    def __init__(self, screen_resolution:pygame.Vector2, current_level:str, current_level_background:str, current_character_skin:str, death_path:str, jump_path:str, tiles_path:list, screen:pygame.Surface) -> None:
        self.__screen_resolution:pygame.Vector2 = screen_resolution
        self.__current_level:str = current_level
        self.__current_level_background:str = current_level_background
        self.__current_character_skin:str = current_character_skin
        self.__death_path:str = death_path
        self.__jump_path:str = jump_path
        self.__tiles_path:str = tiles_path
        self.__screen:pygame.Surface = screen

    def game_loop(self) -> str:
        """
        Loop used for the game. Returns "pausemenu" on specific input, otherwise runs indefinetly.
        """

        # loop
        main_loop = Game(
            self.__screen_resolution,
            self.__current_level,
            self.__current_level_background,
            self.__current_character_skin,
            self.__death_path,
            self.__jump_path,
            self.__tiles_path)

        main_loop.running(self.__screen)

        if main_loop.win:
            return "winmenu"

        if main_loop.hardEscape:
            return "quit"

        return "mainmenu"
