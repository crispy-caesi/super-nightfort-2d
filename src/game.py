# ===================== import ===================== #

import pygame
from tile_map import TileMap
from player import Player
from inputs import KeyInput
from PIL import Image, ImageSequence

from audio import MusicController

# ===================== Main ===================== #

class Game():
    """
    Class that fuses all of the subparts together for the game to be playable.
    """

    def __init__(self, screenResolution :pygame.math.Vector2, currentLevel :str, backgroundImagePath :str, currentCharacterSkinPath :str, deathImagePath :str, jumpImagePath :str, tilesPath:list, key_input:KeyInput):
        pygame.mixer.pre_init(44100,16,3,4096)
        pygame.init()
        self.__screenResolution = screenResolution
        self.__tileMap = TileMap(currentLevel,tilesPath)
        self.__hurtMap = self.__tileMap.hurt_map
        
        images = self.loadGIF(currentCharacterSkinPath)
        deathImages=self.loadGIF(deathImagePath)
        jumpImgages = self.loadGIF(jumpImagePath)
        self.__player = Player(images=images, deathImages= deathImages, jumpImages= jumpImgages)
        self.__allSprites = pygame.sprite.Group()
        self.__allSprites.add(self.__tileMap)

        self.__allSprites.add(self.__player)
        self.__allSprites.add(self.__player.verticalCollisionBox)
        self.__allSprites.add(self.__player.horizontalCollisionBox)
        self.__background = pygame.image.load(backgroundImagePath).convert()
        self.__background = pygame.transform.scale(self.__background,(self.__screenResolution))
        self.__keyInput = key_input
        self.__clock = pygame.time.Clock()

        self.__win = False
        self.__hardEscape = False

    def running(self, screen: pygame.surface.Surface):
        """
        Method to run the game.
        """
        
        running = True
        musicController = MusicController("sprites/soundsAndMusic/inGameBackgroundMusic.wav")
        musicController.play()


        while running:
            # input update
            self.__keyInput.getInput()
            # condition to end the running process
            if self.__keyInput.key_escape or self.__player.isDead:
                self.__keyInput.key_escape = False
                running = False

            if self.__keyInput.key_hard_escape:
                self.__hardEscape = True
                running = False
            
            if self.__player.win:
                self.__win = True
                running = False

            self.frameUpdate(self.__keyInput, screen)
            
            self.__clock.tick(60)

        self.resetHurtmap()
        # after the loop is done, return to main menu
        musicController.stop()

    @property
    def win(self):
        return self.__win
    
    @property
    def hardEscape(self):
        return self.__hardEscape

    def resetHurtmap(self):
        """
        Method to reset the hurtmap.
        """
        
        self.__hurtMap = None

    def drawGameFrame(self):
        """
        Method to blit the game on the screen.
        """
                
        # camera - calculate the offset
        playerOffsetX = self.__screenResolution.x // 6 - self.__player.rect.centerx # more on the left site
        playerOffsetY = self.__screenResolution.y // 2 - self.__player.rect.centery # center
        
        # camera - move all sprites in the other direction
        for __sprite in self.__allSprites:
            __sprite.rect.x += playerOffsetX
            __sprite.rect.y += playerOffsetY

        # draws the current frame on the screen
        self.__screen.blit(self.__background, (0, 0))
        self.__allSprites.draw(self.__screen)
        #TODO UI health
        #TODO UI score
        pygame.display.flip()

    def loadGIF(self,filename :str):
        """
        Extracting the individual frames from the GIF and storing them in a list
        """
        pilImage = Image.open(filename)
        frames = []
        for frame in ImageSequence.Iterator(pilImage):
            frame = frame.convert('RGBA')
            pygameImage = pygame.image.fromstring(
                frame.tobytes(), frame.size, frame.mode).convert_alpha()
            frames.append(pygameImage)
        return frames

# ============== game loop ============== #

    def frameUpdate(self, __input :KeyInput, __screen :pygame.surface.Surface):
        """
        Method that lets the game update.
        """

        # runs all of Game.py main functions
        self.__screen = __screen
        self.__keyInput = __input
        self.__player.playerUpdate(self.__keyInput, self.__tileMap, self.__hurtMap)
        self.__tileMap.update_tilemap_position()
        self.drawGameFrame()
