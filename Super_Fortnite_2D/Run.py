# ===================== import ===================== #

import pygame
import Menu

# ===================== run ===================== #

clock = pygame.time.Clock()
mainmenuloop = Menu.MainMenu()
levelmenuloop = Menu.LevelMenu()
gameloop = Menu.GameLoop()

if __name__ == "__main__":
    currentloop = str("mainmenu")
    while True:
        print(currentloop)
        if currentloop == "mainmenu":
            currentloop = mainmenuloop.mainmenuloop()
        if currentloop == "levelmenu":
            currentloop = levelmenuloop.levelmenuloop()
        if currentloop == "gameloop":
            currentloop = gameloop.gameloop()
        clock.tick(30)