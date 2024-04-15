import pygame

class MusicController():
    def __init__(self) -> None:
       """
       class for an easy controll of the music and sounds in the game
       """
       pass

    def initInGameBackgroundMusic(self, inGameBackgroundMusicPath:str):
        """
        You cannot pass the file path as usual in the constructor 
        because the class can be instantiated at multiple locations, 
        but not all sounds are needed everywhere, which is why the methods for initializing the individual sounds.
        """
        self.__inGameBackgroundMusic = pygame.mixer.Sound(inGameBackgroundMusicPath)        

    def playInGameBackgroundMusic(self):
         """
         play method -> play the sound
         loops = -1 means, that it reapeat for ever -> to stop the stop methods
         """
         self.__inGameBackgroundMusic.play(loops=-1)
    
    def stopInGameBackgroundMusic(self):
        """
        stops the sound
        """
        self.__inGameBackgroundMusic.stop()

    
    def initMenuBackgroundMusic(self, menuBackgroundMusicPath:str):
        self.__MenuBackgroundMusic = pygame.mixer.Sound(menuBackgroundMusicPath)

    def playMenuBackgroundMusic(self):
        self.__MenuBackgroundMusic.play(loops=-1)
    
    def stopMenuBackgroundMusic(self):
        self.__MenuBackgroundMusic.stop()

    
    def initJumpSound(self, jumpSound:str):
        self.__jumpSound = pygame.mixer.Sound(jumpSound)
    
    def playJumpSound(self):
        """
        the jump sound dont need an stop method, because the sound will not be repeated
        """
        self.__jumpSound.play()


#TODO set sounds and music to the same volume