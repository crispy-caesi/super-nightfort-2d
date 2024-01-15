# ===================== import ===================== #

import pygame
import Menu

# ===================== run ===================== #

if __name__ == "__Main__":
    currentloop = "MAINMENU"
    while True:
        if currentloop == "MAINMENU":
            currentloop = Menu.MainMenu()
        if currentloop == "LEVELMENU":
            currentloop = Menu.LevelMenu()
        if currentloop == "GAMELOOP":
            currentloop = Menu.GameLoop()