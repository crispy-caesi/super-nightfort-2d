# ===================== import ===================== #

import pygame
import Menu
import sys

# ===================== main ===================== #

def main():
    """
    Method to run the application.
    """
    
    __clock = pygame.time.Clock()
    __menuloop = Menu.Menu()

    # loop preset
    __currentloop = "mainmenu"

    while True:

        if __currentloop == "mainmenu":
            __currentloop = __menuloop.mainMenuLoop()

        elif __currentloop == "levelmenu":
            __currentloop = __menuloop.levelMenuLoop()
        
        elif __currentloop == "charactermenu":
            __currentloop = __menuloop.characterMenuLoop()

        elif __currentloop == "gameloop":
            __currentloop = __menuloop.gameLoop()

        elif __currentloop == "charactermenu":
            __currentloop = __menuloop.characterMenuLoop()
        
        elif __currentloop == "winmenu":
            __currentloop = __menuloop.winMenuLoop()

        elif __currentloop == "quit":
            pygame.quit()
            sys.exit()
            
        __clock.tick(30)

# ===================== run ===================== #
        
# run the application
if __name__ == "__main__":
    main()