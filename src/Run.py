# ===================== import ===================== #

import pygame
import Menu
import sys
from NewMenu import *

# ===================== main ===================== #

class SupaNiteFort():
    def __init__(self) -> None:
        print("Start Supa Nite Fort")

    def run(self):
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
                currentloop = mainMenu.mainMenuLoop()

            elif currentloop == "levelmenu":
                currentloop = levelMenu.levelMenuLoop()
            
            elif currentloop == "charactermenu":
                currentloop = characterMenu.characterMenuLoop()

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
                currentloop = winMenu.winMenuLoop()

            elif currentloop == "quit":
                pygame.quit()
                sys.exit()
                
            clock.tick(30)

# ===================== run ===================== #
        
# run the application
if __name__ == "__main__":
    supaNiteFort = SupaNiteFort()
    supaNiteFort.run()