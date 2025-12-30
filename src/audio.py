"""module that provides music and sound management"""
import pygame

class MusicController():
    """
    Class handling music, allows to start and stop the music, constructor takes background music file path as an argument. 
    """
    def __init__(self, music_file_path :str) -> None:
        self.__background_music = pygame.mixer.Sound(music_file_path)

    def play(self) -> None:
        """
        Play set background music indefinitely
        """
        self.__background_music.play(loops=-1)    # loops=-1 -> loops indefinitely
    def stop(self) -> None:
        """
        Stops playing background music
        """
        self.__background_music.stop()

class GameSounds():
    """
    Class handling all sound effects played ingame, constructor takes sound effect file path as an argument.
    """
    def __init__(self, jump_sound_file_path :str) -> None:
        self.__jump_sound = pygame.mixer.Sound(jump_sound_file_path)

    def play_jump_sound(self) -> None:
        """
        Plays jump sound once
        """
        self.__jump_sound.play()

#TODO set sounds and music to the same volume
