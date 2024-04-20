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

        # loop preset
        currentloop = "mainmenu"

        while True:

            if currentloop == "mainmenu":
                self.__mainMenu = MainMenu(clock)
                currentloop = self.__mainMenu.mainMenuLoop()

            elif currentloop == "levelmenu":
                self.__levelMenu = LevelMenu(clock)
                currentloop = self.__levelMenu.levelMenuLoop()
            
            elif currentloop == "charactermenu":
                self.__characterMenu = CharacterMenu(clock)
                currentloop = self.__characterMenu.characterMenuLoop()

            elif currentloop == "gameloop":
                gameLoop = GameLoop(
                    screenResolution=self.__levelMenu.getScreenResoltution(),
                    currentLevel=self.__levelMenu.getCurrentLevel(),
                    currentLevelBackground=self.__levelMenu.getCurrentLevelBackground(),
                    currentCharacterSkin=self.__characterMenu.getCurrentCharacterSkin(),
                    death_path=self.__characterMenu.getDeathPath(),
                    jump_path=self.__characterMenu.getJumpPath(),
                    tiles_path=self.__levelMenu.getTilesPath(),
                    screen=self.__levelMenu.getScreen()
                )
                currentloop = gameLoop.gameLoop()
            
            elif currentloop == "winmenu":
                winMenu = WinMenu()
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