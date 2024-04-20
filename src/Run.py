# ===================== import ===================== #

import pygame
from Menu import *
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
                screenResolution=levelMenu.getScreenResoltution(),
                currentLevel=levelMenu.getCurrentLevel(),
                currentLevelBackground=levelMenu.getCurrentLevelBackground(),
                currentCharacterSkin=characterMenu.getCurrentCharacterSkin(),
                death_path=characterMenu.getDeathPath(),
                jump_path=characterMenu.getJumpPath(),
                tiles_path=levelMenu.getTilesPath(),
                screen=levelMenu.getScreen()
            )
            currentloop = gameLoop.gameLoop()
        
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