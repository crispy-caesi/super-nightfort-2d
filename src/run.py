"""the game starts from this module"""
# ===================== import ===================== #
import sys
import pygame
from inputs import KeyInput
from menu import MainMenu, LevelMenu, CharacterMenu, WinMenu, GameLoop

# ===================== run ===================== #

def run() -> None:
    """
    Method to run the application.
    """
    pygame.display.init()
    screen:pygame.Surface = pygame.display.set_mode()
    screen_resolution:pygame.Vector2 = pygame.Vector2(screen.get_size()[0], screen.get_size()[1]) #[0] is x, [1] is y


    key_input = KeyInput()

    clock = pygame.time.Clock()
    main_menu = MainMenu(clock, screen, screen_resolution, key_input)
    level_menu = LevelMenu(clock, screen, screen_resolution, key_input)
    character_menu = CharacterMenu(clock, screen, screen_resolution, key_input)
    win_menu = WinMenu(screen, screen_resolution, key_input)


    # loop preset
    currentloop = "mainmenu"

    while True:

        if currentloop == "mainmenu":
            main_menu.draw()
            currentloop = main_menu.loop()

        elif currentloop == "levelmenu":
            level_menu.draw()
            currentloop = level_menu.loop()

        elif currentloop == "charactermenu":
            character_menu.draw()
            currentloop = character_menu.loop()

        elif currentloop == "gameloop":
            game_loop = GameLoop(
                screen_resolution=level_menu.get_screen_resoltution(),
                current_level=level_menu.get_current_level(),
                current_level_background=level_menu.get_current_level_background(),
                current_character_skin=character_menu.get_current_character_skin(),
                death_path=character_menu.get_death_path(),
                jump_path=character_menu.get_jump_path(),
                tiles_path=level_menu.get_tiles_path(),
                screen=level_menu.get_screen(),
                key_input=key_input
            )
            currentloop = game_loop.game_loop()

        elif currentloop == "winmenu":
            win_menu.draw()
            currentloop = win_menu.loop()

        elif currentloop == "quit":
            pygame.quit()
            sys.exit()

        clock.tick(30)

# ===================== run ===================== #

# run the application
if __name__ == "__main__":
    run()
