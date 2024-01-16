# ===================== import ===================== #

import pygame
import Menu
import sys

# ===================== run ===================== #

clock = pygame.time.Clock()
menuloop = Menu.Menu()



if __name__ == "__main__":
    currentloop = "mainmenu"
    while True:
        #print(currentloop)
        if currentloop == "mainmenu":
            currentloop = menuloop.mainmenuloop()
        if currentloop == "levelmenu":
            currentloop = menuloop.levelmenuloop()
        #if currentloop == "gameloop":
            #currentloop = Menu.GameLoop()
        if currentloop == "quit":
            pygame.quit()
            sys.exit()
            
        clock.tick(30)