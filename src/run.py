# ===================== import ===================== #

import pygame
from menu import *
import sys

# ===================== run ===================== #

def run() -> None:
    """
    Method to run the application.
    """
    
    clock = pygame.time.Clock()
    mainMenu = MainMenu(clock)
    levelMenu = LevelMenu(clock)
    characterMenu = CharacterMenu(clock)
    winMenu = WinMenu()


    # loop preset
    currentloop = "mainmenu"

    while True:

        if currentloop == "mainmenu":
            mainMenu.draw()
            currentloop = mainMenu.loop()

        elif currentloop == "levelmenu":
            levelMenu.draw()
            currentloop = levelMenu.loop()
        
        elif currentloop == "charactermenu":
            characterMenu.draw()
            currentloop = characterMenu.loop()

        elif currentloop == "gameloop":
            gameLoop = GameLoop(
                screen_resolution=levelMenu.get_screen_resoltution(),
                current_level=levelMenu.get_current_level(),
                current_level_background=levelMenu.get_current_level_background(),
                current_character_skin=characterMenu.get_current_character_skin(),
                death_path=characterMenu.get_death_path(),
                jump_path=characterMenu.get_jump_path(),
                tiles_path=levelMenu.get_tiles_path(),
                screen=levelMenu.get_screen()
            )
            currentloop = gameLoop.game_loop()
        
        elif currentloop == "winmenu":
            winMenu.draw()
            currentloop = winMenu.loop()

        elif currentloop == "quit":
            pygame.quit()
            sys.exit()
            
        clock.tick(30)

# ===================== run ===================== #
        
# run the application
if __name__ == "__main__":
    run()