import pygame

class MusicController():
    """
    Class handling music, allows to start and stop the music, constructor takes background music file path as an argument. 
    """
    def __init__(self, musicFilePath :str):
        self.__backgroundMusic = pygame.mixer.Sound(musicFilePath)

    def play(self):
        """
        Play set background music indefinitely
        """
        self.__backgroundMusic.play(loops=-1)    # loops=-1 -> loops indefinitely
    def stop(self):
        """
        Stops playing background music
        """
        self.__backgroundMusic.stop()

class GameSounds():
    """
    Class handling all sound effects played ingame, constructor takes sound effect file path as an argument.
    """
    def __init__(self, jumpSoundFilePath :str):
        self.__jumpSound = pygame.mixer.Sound(jumpSoundFilePath)

    def playJumpSound(self):
        """
        Plays jump sound once
        """
        self.__jumpSound.play()

#TODO set sounds and music to the same volume
