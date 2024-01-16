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
            currentloop = menuloop.mainmenuloop()

        elif currentloop == "levelmenu":
            currentloop = menuloop.levelmenuloop()

        elif currentloop == "gameloop":
            currentloop = menuloop.gameloop()

        elif currentloop == "quit":
            pygame.quit()
            sys.exit()
            
        clock.tick(60)

# ===================== run ===================== #
        
# run the application
if __name__ == "__main__":
    main()