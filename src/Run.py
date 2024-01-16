# ===================== import ===================== #

import pygame
import Menu
import sys

# ===================== main ===================== #

def main():
    """
    Method to run the application.
    """
    
    clock = pygame.time.Clock()
    menuloop = Menu.Menu()

    # loop preset
    currentloop = "mainmenu"

    while True:

        if currentloop == "mainmenu":
            currentloop = menuloop.mainMenuLoop()

        elif currentloop == "levelmenu":
            currentloop = menuloop.levelMenuLoop()

        elif currentloop == "gameloop":
            currentloop = menuloop.gameLoop()

        elif currentloop == "quit":
            pygame.quit()
            sys.exit()
            
        clock.tick(60)

# ===================== run ===================== #
        
# run the application
if __name__ == "__main__":
    main()